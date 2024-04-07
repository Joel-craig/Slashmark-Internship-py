import random 
import time

def intro():
    print("We are going to play a game. I am thinking of a number between 1 and 100")
    time.sleep(0.5)
    print("Go ahead. Guess!")

def pick():
    number = random.randint(1, 100)  # Pick the number between 1 and 100
    guessesTaken = 0
    while guessesTaken < 100:  # If the number of guesses is less than 100
        time.sleep(0.25)
        enter = input("Guess: ")  # Inserts the place to enter guess
        try:  # Check if a number was entered
            guess = int(enter)  # Stores the guess as an integer instead of a string    

            if 1 <= guess <= 100:  # If they are in range
                guessesTaken += 1  # Adds one guess each time the player is wrong
                if guessesTaken < 100:
                    if guess < number:
                        print("The guess of the number that you have entered is too low")
                    elif guess > number:
                        print("The guess of the number that you have entered is too high")
                    else:
                        print("Good job! You guessed the number.")
                        break
                    print("Try Again!")
            else:  # If they aren't in the range
                print("That number isn't in the range!")
                time.sleep(0.25)
                print("Please enter a number between 1 and 100")

        except ValueError:  # If a number wasn't entered
            print("I don't think that " + enter + " is a number. Sorry")

    if guess != number:
        print('Nope. The number I was thinking of was ' + str(number))

playagain = "yes"
while playagain.lower() in ["yes", "y"]:
    intro()
    pick()
    playagain = input("Do you want to play again? (yes/no): ")
