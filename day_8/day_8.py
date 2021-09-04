import math
################
# Exercise 8.1 #
################

# Write your code below this line 👇


def paint_calc(height, width, cover):
    cans_paint = math.ceil((width * height) / cover)
    print(f'You\'ll need {cans_paint} cans of paint')

# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.


# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

################
# Exercise 8.2 #
################

# Write your code below this line 👇


def prime_checker(number):
    is_prime = True
    if number == 1:
        is_prime = False
    else:
        for num in range(2, number):
            if number % num == 0:
                is_prime = False
                break
    if is_prime:
        print('It\'s a prime number.')
    else:
        print('It\'s not a prime number.')

# Write your code above this line 👆


# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
