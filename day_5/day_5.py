################
# Exercise 5.1 #
################

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
sum = 0
count = 0

for num in student_heights:
    sum += num
    count += 1

avg = round(sum / count)

print(avg)

################
# Exercise 5.2 #
################

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
max = 0

for score in student_scores:
    if score > max:
        max = score

print(f"The highest score is: {max}")

################
# Exercise 5.3 #
################

sum = 0

for num in range(2, 101, 2):
    sum += num

print(sum)

################
# Exercise 5.4 #
################

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
