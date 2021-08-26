################
# Exercise 2.1 #
################

value = input('Enter a two digit number (i.e. 24) ')

print('Total of each digit is: ', int(value[0]) + int(value[1]))

################
# Exercise 2.2 #
################

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = int(weight) / (float(height) ** 2)
print(int(bmi))

################
# Exercise 2.3 #
################

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
years = 90 - int(age)
days = years * 365
weeks = years * 52
months = years * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
