import random
import hangman_art as art
import hangman_words as words

stages = art.stages

end_of_game = False
word_list = words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

# Testing code
print(f"Pssst, the solution is {chosen_word}.")

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

print(art.logo)

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've guessed {guess} already.")

    # Check guessed letter
    if guess not in chosen_word:
        print(f"{guess} is not in the word.")
        lives -= 1
        if lives == 0:
            print("You lose.")
            end_of_game = True
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
