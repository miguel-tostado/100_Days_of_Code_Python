import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hand = [rock, paper, scissors]
hands = ['rock', 'paper', 'scissors']

userInput = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
npcInput = random.randint(0, 2)

if userInput > 2:
    print('Enter a valid number.')
    exit()
else:
    userHand = hands[userInput]
    npcHand = hands[npcInput]

    print(f"You chose {userHand}\n{hand[userInput]}")
    print(f"NPC chose {npcHand}\n{hand[npcInput]}")

    if userHand == npcHand:
        print('Draw')
    elif userHand == 'rock':
        if npcHand == 'paper':
            print('You lose.')
        else:
            print('You win!')
    elif userHand == 'paper':
        if npcHand == 'scissors':
            print('You lose.')
        else:
            print('You win!')
    elif userHand == 'scissors':
        if npcHand == 'rock':
            print('You lose.')
        else:
            print('You win!')
