import cv2
import numpy as np
import pytesseract

# Function to detect license plates in a frame
def detect_license_plate(frame):
    # Preprocess the frame (e.g., convert to grayscale, apply Gaussian blur, etc.)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Detect edges using Canny edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours of objects in the edge-detected image
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through contours and filter for potential license plate regions
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:  # Adjust this threshold based on your specific use case
            x, y, w, h = cv2.boundingRect(contour)
            license_plate_region = frame[y:y+h, x:x+w]

            # Perform OCR on the potential license plate region
            license_plate_text = recognize_license_plate(license_plate_region)

            # Draw a bounding box around the license plate region
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display the recognized license plate text
            cv2.putText(frame, license_plate_text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

# Function to recognize license plate text using OCR
def recognize_license_plate(license_plate_region):
    # Apply OCR using Tesseract OCR engine
    license_plate_text = pytesseract.image_to_string(license_plate_region)

    return license_plate_text

# Main function for real-time license plate recognition
def main():
    # Open a video stream (e.g., from a camera)
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the video stream
        ret, frame = cap.read()
        if not ret:
            break

        # Detect license plates in the frame
        frame_with_license_plates = detect_license_plate(frame)

        # Display the frame with license plate detection
        cv2.imshow('License Plate Recognition', frame_with_license_plates)

        # Check for 'q' key to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video stream and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
