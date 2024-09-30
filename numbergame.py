import random

def number_guessing_game():
    """A number guessing game where the computer randomly selects a number
    within a specified range, and the player tries to guess it.

    Args:
        None

    Returns:
        None
    """

    # Set the range for the random number
    min_value = 1
    max_value = 100

    # Generate a random number within the specified range
    secret_number = random.randint(min_value, max_value)

    # Initialize the number of attempts
    attempts = 0

    print(f"I'm thinking of a number between {min_value} and {max_value}. Can you guess it? 🤔")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            attempts += 1

            if guess < secret_number:
                print("Too low! 🙁")
            elif guess > secret_number:
                print("Too high! 😮")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts. 🎉")
                break

        except ValueError:
            print("Invalid input. Please enter a number. ❌")

    # Ask if the player wants to play again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        number_guessing_game()

# Start the game
number_guessing_game()