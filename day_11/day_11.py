from art import logo
import os
import random


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def draw_card():
    return random.choice(deck)


def check_scores(user_score, computer_score):
    if user_score > 21:
        print('You lose!')
        return -1
    elif computer_score > 21 and user_score <= 21:
        print('You win!')
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


def blackjack():
    user_hand = []
    user_score = 0

    computer_hand = []
    computer_score = 0

    is_game_over = False

    for card in range(2):
        user_hand.append(draw_card())
        user_score += int(user_hand[card])
        computer_hand.append(draw_card())
        computer_score += int(user_hand[card])

    count = 0
    rounds = 2

    cls()
    print(logo)

    while not is_game_over and count <= rounds:
        print(
            f"Your cards: {user_hand}, current user_score: {user_score}")
        print(f"Computer's first card: {computer_hand[0]}")

        hit = 'y'  # input("Type 'y' to get another card, type 'n' to pass: ")

        if hit == 'y':
            count += 1

            card = draw_card()
            user_hand.append(card)
            user_score += card
            score_check = check_scores(user_score, computer_score)
            if score_check < 0:
                is_game_over = True

        else:
            print(f"Your final hand: {user_hand}, final score: {user_score}")
            print(
                f"Computer's final hand: {computer_hand}, final score: {computer_score}")
            check_scores(user_score, computer_score)

            # input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
            restart = 'n'
            if restart == 'y':
                blackjack()
            else:
                is_game_over = True
                break


# input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
game_start = 'y'
if game_start == 'y':
    blackjack()
