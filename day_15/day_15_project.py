from data import MENU, resources, coin_value


def print_report():
    """Prints each resource on a separate line and shows its current quantity."""
    for resource in resources:
        if resource == "money":
            print(f"{resource}: {resources[resource][1]}{resources[resource][0]}")
        else:
            print(f"{resource}: {resources[resource][0]}{resources[resource][1]}")


def check_resources(coffee_selection):
    """Takes the user's coffee selection and determines if there's enough resources to make it.

    Args:
        coffee_selection (str): 'espresso', 'latte', 'cappuccino'

    Returns:
        str: If a resource is running low, returns the resource as a string.
        bool: If sufficient resource are available, returns True
    """
    coffee = {}
    for flavor in MENU:
        if flavor == coffee_selection:
            coffee = MENU[flavor]
    for resource in resources:
        if resource != "money":
            ingredient_compare = coffee["ingredients"][resource][0]
            if ingredient_compare > resources[resource][0]:
                return resource
    return True


def reduce_resources(coffee_selection):
    """Once we've verified the sum of coins entered is sufficient to purchase a selected coffee, we reduce the amount of ingredients needed to make the coffee from our available resources.

    Args:
        coffee_selection (str): 'espresso', 'latte', 'cappuccino'
    """
    coffee = MENU[coffee_selection]["ingredients"]
    for resource in resources:
        if resource != "money":
            resources[resource][0] -= coffee[resource][0]
        elif resource == "money":
            resources[resource][0] += MENU[coffee_selection]["price"]


is_coffee_served = False

while not is_coffee_served:
    user_coins = {"quarters": 0, "dimes": 0, "nickles": 0, "pennies": 0}
    total_coin_value = 0
    change_back = 0
    revenue = 0

    low_resource = []

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
        print_report()
    elif user_input in MENU:
        resource_check_result = check_resources(user_input)
        if resource_check_result == True:
            print("Please insert coins.")
            for coin in coin_value:
                num_coin = float(input(f"How many {coin}?: "))
                user_coins[coin] = num_coin
                total_coin_value += coin_value[coin] * num_coin
            change_back = total_coin_value - MENU[user_input]["price"]

            if change_back >= 0:
                reduce_resources(user_input)
                print(f"Here is ${change_back:.2f} in change.")
                print(f"Here is your {user_input} ☕Enjoy!")
            else:
                print(
                    f"Sorry, you don't have enough for this flavor. You're short ${change_back * -1}."
                )
        else:
            low_resource.append(resource_check_result)
            for resource in low_resource:
                print(f"Sorry there is not enough {resource}")
    else:
        print("Invalid entry, please try again.")
