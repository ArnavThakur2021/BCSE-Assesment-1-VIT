import random

def guess_number():
    # Generate a random number between 1 and 20
    secret_number = random.randint(1, 20)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 20.")

    while True:
        try:
            # Get the user's guess
            guess = int(input("Take a guess: "))
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Your guess is too low.")
            elif guess > secret_number:
                print("Your guess is too high.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Start the game
guess_number()