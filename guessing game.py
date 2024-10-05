import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)

    # Initialize the number of attempts
    attempts = 0

    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        # Ask the user for their guess
        user_guess = input("Take a guess: ")

        # Check if the user wants to quit
        if user_guess.lower() == "quit":
            print("Okay, the number was {}.".format(number_to_guess))
            break

        # Try to convert the user's guess to an integer
        try:
            user_guess = int(user_guess)
        except ValueError:
            print("That's not a valid number!")
            continue

        # Increment the number of attempts
        attempts += 1

        # Check if the user's guess is correct
        if user_guess == number_to_guess:
            print("Congratulations! You found the number in {} attempts.".format(attempts))
            break
        elif user_guess < number_to_guess:
            print("Higher!")
        else:
            print("Lower!")

if __name__ == "__main__":
    number_guessing_game()
