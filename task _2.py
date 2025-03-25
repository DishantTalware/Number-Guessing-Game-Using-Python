# Task 2: Number Guessing Game
# Develop a Python game where the user guesses a randomly generated number between 1 and 100.
#------------------------------------------------------------------------------------------------------



import random

def number():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a random number between 1 and 100.")
    print("Your task is to guess the number!")

    number_to_guess = random.randint(1, 100)

    attempts = 0
    guess = None
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))  
            attempts += 1  

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts.")

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    number()
