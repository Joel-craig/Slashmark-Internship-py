import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print("You:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        print("Sorry, there was an error with the speech recognition service.")
        return ""

def main():
    speak("Hello! I am your Python voice assistant. How can I help you today?")
    while True:
        query = listen().lower()

        if "hello" in query:
            speak("Hello there!")

        elif "how are you" in query:
            speak("I'm doing well, thank you for asking!")

        elif "what time is it" in query:
            speak("It's time to learn some Python!")

        elif "goodbye" in query or "bye" in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
