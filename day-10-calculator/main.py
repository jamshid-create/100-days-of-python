from art import logo

def add(n1, n2):

    return n1 + n2

def subtract(n1, n2):

    return n1 - n2

def multiply(n1, n2):

    return n1 * n2

def divide(n1, n2):

    return n1 / n2

def calculator():

    print(logo)

    should_accumulate = True

    num1 = float(input("What's the first number?: "))

    while should_accumulate:

        for symbol in operations:

            print(symbol)

        operation_symbol = input("pick an operation: ")

        num2 = float(input("What's the next number?: "))

        answer = operations[operation_symbol](n1= num1, n2= num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":

            num1 = answer

        elif choice == "n":

            should_accumulate = False

            print("\n" * 20)

            calculator()

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

calculator()
