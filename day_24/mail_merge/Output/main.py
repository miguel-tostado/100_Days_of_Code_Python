names_list = "../Input/Names/invited_names.txt"
letter_boilerplate = "../Input/starting_letter.txt"

with open(names_list, "r") as names:
    names = names.read().split()

with open(letter_boilerplate, "r") as letter:
    boilerplate = letter.read()

for name in names:
    letter = boilerplate.replace("[name]", f"{name}")
    with open(f"ReadyToSend/letter_for_{name}", mode="w") as finished_letter:
        finished_letter.write(letter)
