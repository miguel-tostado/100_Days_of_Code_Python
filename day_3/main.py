################
# Exercise 3.1 #
################

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
num_mod = number % 2

if num_mod == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

################
# Exercise 3.2 #
################

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = weight / height ** 2

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are Underweight")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")

################
# Exercise 3.3 #
################

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    if year % 100 == 0 and year % 400 == 0:
        print("Leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")

################
# Exercise 3.4 #
################

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill += 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill += 25
    if add_pepperoni == "Y":
        bill += 3
else:
    print("Please select a pizza size.")

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")

################
# Exercise 3.5 #
################

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = "Brad Pitt"  # input("What is your name? \n")
name2 = "Jennifer Aniston"  # input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
combined_name = name1.lower() + name2.lower()

t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")

l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")

true_total = t + r + u + e
love_total = l + o + v + e
love_score = str(true_total) + str(love_total)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) > 40 and int(love_score) < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
