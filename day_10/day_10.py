#################
# Exercise 10.1 #
#################

def is_leap(year):
    """Returns True or False if the given year is a leap year.

    Args:
        year (int): User given year

    Returns:
        bool: True or False if a given year is a leap year.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """Returns how many days are within in a month and calls is_leap(year) to determine if the year is a leapyear and February should have an additional day.add()

    Args:
        year (int): Year used in is_leap(year).
        month (int): Month number used to determine number of days.

    Returns:
        int: Number of days in a given month.
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month - 1]


# 🚨 Do NOT change any of the code below
year = 2020  # int(input("Enter a year: "))
month = 2  # int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
