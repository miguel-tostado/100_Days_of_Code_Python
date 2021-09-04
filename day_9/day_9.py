################
# Exercise 9.1 #
################

student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    grade = ''
    if score < 70:
        grade = 'Fail'
    elif score < 80:
        grade = 'Acceptable'
    elif score < 90:
        grade = 'Exceeds Expectations'
    elif score <= 100:
        grade = 'Outstanding'
    student_grades[student] = grade

# 🚨 Don't change the code below 👇
print(student_grades)

################
# Exercise 9.2 #
################

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]
# 🚨 Do NOT change the code above

# to be added to the travel_log. 👇


def add_new_country(country, visits, cities):
    new_entry = {'country': country, 'visits': visits, 'cities': cities}
    travel_log.append(new_entry)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
