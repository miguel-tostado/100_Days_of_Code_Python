from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def divide(n1, n2):
    return n1 / n2


def multiply(n1, n2):
    return n1 * n2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}


def calculator():
    print(logo)

    num1 = float(input("What's the first number?: "))
    for operator in operations:
        print(operator)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        more_calcs = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: "
        )

        if more_calcs == "n":
            should_continue = False
            calculator()
        else:
            num1 = answer


calculator()
