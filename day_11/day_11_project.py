from art import logo
import os
import random


def cls():
    os.system("cls" if os.name == "nt" else "clear")


deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    return random.choice(deck)


def update_scores(hand):
    return sum(hand)


def check_scores(user_score, computer_score):
    if user_score > 21:
        print("You lose!")
        return -1
    elif computer_score > 21 and user_score <= 21:
        print("You win!")
        return 1
    elif user_score == computer_score:
        print("Draw")
        return 0
    elif user_score > computer_score or user_score == 21:
        print("You win!")
        return 1
    else:
        print("You lose!")
        return -1


def end_game(user_hand, user_score, computer_hand, computer_score):
    print(f"Your final hand: {user_hand}, final score: {user_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")
    check_scores(user_score, computer_score)
    restart = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if restart == "y":
        return True
    else:
        exit()


def blackjack():
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
