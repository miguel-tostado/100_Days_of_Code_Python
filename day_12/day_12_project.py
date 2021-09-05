from art import logo
import random
import os


def cls():
    """Clears the screen. Used each time a new game starts"""
    os.system("cls" if os.name == "nt" else "clear")


def set_difficulty(game_difficulty):
    """Accepts the "easy" or "hard" difficulty and returns the number of attempts a player has.

    Args:
        game_difficulty (str): "easy" or "hard"

    Returns:
        int: 5 or 10
    """
    difficulty = game_difficulty
    while difficulty != "easy" or difficulty != "hard":
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Invalid choice.")
            difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()


def new_game():
    """Asks the player if they want to play again.

    Returns:
        bool: True if the player wants to play again, False otherwise.
    """
    restart = input("Do you want to play again? Type 'yes' or 'no' ").lower()
    if restart == "yes":
        return True
    else:
        return False


def guess_number(game_attempts):
    """Starts the game with the number of attempts a player has as an input

    Args:
        game_attempts (int): Number of attempts a player has. Determined by difficulty.

    Returns:
        bool: True if the player wants to play again, False otherwise.
    """
    num_to_guess = random.randint(1, 101)
    attempts = game_attempts

    while attempts > 0:
        print(f"You have {attempts} attempts remaining ")
        player_guess = int(input("Make a guess: "))
        if player_guess == num_to_guess:
            print(f"You got it! The answer was {num_to_guess}")
            return new_game()
        elif player_guess > num_to_guess:
            print("Too high.")
        elif player_guess < num_to_guess:
            print("Too low.")

        attempts -= 1

        if attempts > 0:
            print("Guess again.")

    if attempts <= 0:
        print("You've run out of attempts.")
        return new_game()
    return new_game()


restart = True

while restart:
    cls()
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    game_difficulty = input("Choose a difficulty. Type 'easy' or 'hard: ").lower()
    game_attempts = set_difficulty(game_difficulty)

    restart = guess_number(game_attempts)
