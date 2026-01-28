import random

# Starter code for Number Guessing Game

def play_game():
    """
    Main game function. Generates a random number and handles the guessing logic.
    TODO: Complete this function
    """
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")
    
    # TODO: Add your game loop here
    # Hint: Use a while loop to keep asking for guesses
    # Remember to:
    # - Get user input
    # - Convert input to integer
    # - Check if guess is correct, too high, or too low
    # - Track number of attempts
    # - Handle invalid input
    
    pass


def play_again():
    """
    Ask the player if they want to play again.
    TODO: Complete this function
    """
    # TODO: Ask user if they want to play again
    # Return True or False
    pass


# Main program
if __name__ == "__main__":
    # TODO: Call play_game() and handle replay logic
    play_game()
