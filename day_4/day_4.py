import random

################
# Exercise 4.1 #
################


def coinFlip():
    coinSide = random.randint(0, 1)

    if coinSide == 0:
        return "Tails"
    else:
        return "Heads"


print(coinFlip())

################
# Exercise 4.2 #
################

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
print(names[random.randint(0, len(names) - 1)] + " is going to buy the meal today!")

################
# Exercise 4.3 #
################

# 🚨 Don't change the code below 👇
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
column = int(position[0])
row = int(position[1])

map[row - 1][column - 1] = "X"
# Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
