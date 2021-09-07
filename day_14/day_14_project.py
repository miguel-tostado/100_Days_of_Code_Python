import random
import os
from art import logo, vs
from game_data import data


def cls():
    """Clears the screen between comparisons"""
    os.system("cls" if os.name == "nt" else "clear")


def get_person():
    """Randomly selects a random Instagram account from the data list and returns a dictionary

    Returns:
        dict: Dictionary containing an account's 'name', 'follower_count', 'description', and 'country'
    """
    return data[random.randint(0, len(data) - 1)]


def check_input(input, compare_a, compare_b):
    """Determines which account has the highest number of followers then compares the result with 'input'

    Args:
        input (str): 'A' or 'B'
        compare_a (dict): Account A dictionary
        compare_b (dict): Account B dictionary

    Returns:
        bool: True if user input matches whichever account has the highest number of followers.
    """
    highest = ""
    if compare_a["follower_count"] > compare_b["follower_count"]:
        highest = "A"
    elif compare_b["follower_count"] > compare_a["follower_count"]:
        highest = "B"
    else:
        print("Draw!")
        end_game()

    if highest == input:
        return True
    else:
        return False


def end_game():
    """Checks if the user wants to play again

    Returns:
        bool: True if they want to continue, False otherwise
    """
    check_restart = input("Do you want to play again? Type 'Y' or 'N' ").upper()
    if check_restart == "Y":
        return True
    else:
        return False


game_over = False

while not game_over:
    score = 0
    compare_a = get_person()
    compare_b = {}

    continue_game = True

    while continue_game:
        cls()
        print(logo)

        compare_b = get_person()
        while compare_a["name"] == compare_b["name"]:
            compare_b = get_person()

        if score != 0:
            print(f"You're right! Current score: {score}")
        print(
            f"Compare A: {compare_a['name']}, a {compare_a['description']}, from {compare_a['country']}\n"
        )
        print(vs)
        print(
            f"Against B: {compare_b['name']}, a {compare_b['description']}, from {compare_b['country']}"
        )

        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
        answer = check_input(user_input, compare_a, compare_b)
        if answer == True:
            score += 1
            compare_a = compare_b
        else:
            cls()
            print(f"Sorry, that's wrong. Final score: {score}")
            score = 0
            compare_a = get_person()
            continue_game = end_game()

    game_over = True
