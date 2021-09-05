print("Welcome to the tip calculator.")
bill_total = input("What is the total bill? $")
num_people = input("How many people to split the bill? ")
tip_percent = input("What percentage tip would you like to give? 10, 12, or 15? ")

payment = float(bill_total) / int(num_people) * (1 + int(tip_percent) / 100)

print("Each person should pay: $%.2f" % (payment))
