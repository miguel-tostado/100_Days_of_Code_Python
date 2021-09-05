from art import logo
import os
import random


def cls():
    """Clears the screen to make everything look cleaner each game"""
    os.system("cls" if os.name == "nt" else "clear")


deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    """Selects a random card from the deck list

    Returns:
        int: Random card from the deck list
    """
    return random.choice(deck)


def update_scores(hand):
    """Calculates the sum of each card in a hand

    Args:
        hand (list): List of each card in a hand

    Returns:
        int: Sum of each card's value in a hand
    """
    return sum(hand)


def verify_win_conditions(user_score, computer_score):
    """Determines whether the player won, lost, or the game ends in a draw

    Args:
        user_score (int): User's score
        computer_score (int): Computer's score
    """
    if user_score > 21:
        print("You lose!")
    elif computer_score > 21 and user_score <= 21:
        print("You win!")
    elif user_score == computer_score:
        print("Draw")
    elif user_score > computer_score or user_score == 21:
        print("You win!")
    else:
        print("You lose!")


def end_game(user_hand, user_score, computer_hand, computer_score):
    """Prints the end-game messages and asks user if they want to play another game

    Args:
        user_hand (list): User's final hand
        user_score (int): User's final score
        computer_hand (list): Computer's final hand
        computer_score (int): Computer's final score

    Returns:
        bool: If the user wants to play a new game, returns True. Otherwise the program ends.
    """
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    verify_win_conditions(user_score, computer_score)
    restart = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if restart == "y":
        return True
    else:
        exit()


def blackjack():
    """Initiate's a game of Blackjack

    Returns:
        bool: if the game is over, returns True. Otherwise returns False to continue the current game.
    """
    user_hand = []
    user_score = 0

    computer_hand = []
    computer_score = 0

    is_game_over = False

    for card in range(2):
        user_hand.append(deal_card())
        computer_hand.append(deal_card())
    user_score = update_scores(user_hand)
    computer_score = update_scores(computer_hand)

    while computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = update_scores(computer_hand)

    cls()
    print(logo)

    while not is_game_over:
        print(f"Your cards: {user_hand}, current user_score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        if user_score == 21:
            is_game_over = end_game(
                user_hand, user_score, computer_hand, computer_score
            )
        else:
            hit = input("Type 'y' to get another card, type 'n' to pass: ")
            if hit == "y" and user_score < 21:
                user_hand.append(deal_card())
                user_score = update_scores(user_hand)
                if user_score >= 21:
                    is_game_over = end_game(
                        user_hand, user_score, computer_hand, computer_score
                    )
            else:
                is_game_over = end_game(
                    user_hand, user_score, computer_hand, computer_score
                )
    return is_game_over


restart = True
game_start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while restart:
    if game_start == "y":
        restart = blackjack()
    else:
        exit()
