from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while is_on:
    user_input = input(f"What would you like? {menu.get_items()} ").lower()
    drink = menu.find_drink(user_input)
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif drink != None:
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffee_maker.make_coffee(drink)
