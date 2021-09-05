from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]

print(logo)


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = 0
            if cipher_direction == "encode":
                new_position = position + shift_amount
                if new_position >= len(alphabet):
                    new_position = position - (len(alphabet) - shift_amount)
            elif cipher_direction == "decode":
                new_position = position - shift_amount
                if new_position < 0:
                    new_position = len(alphabet) + position - shift
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f"The {cipher_direction}d text is {end_text}")


restart = True

while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26
    caesar(text, shift, direction)
    redo = input("Would you like to go again? (y/n):\n").lower()
    if redo == "n":
        print("Goodbye")
        restart = False
