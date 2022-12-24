# This function adds two numbers
def add(x, y):
    return x + y


# This function subtracts two numbers
def subtract(x, y):
    return x - y


# This function multiplies two numbers
def multiply(x, y):
    return x * y


# This function divides two numbers
def divide(x, y):
    return x / y


# Dictionary to represent the different operations
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    is_running = True
    print("\nWelcome to Calculator")
    num1 = float(input("\nWhat is the first number?:"))

    while is_running:
        operation_symbol = input("\nSelect an operation:\n+\n-\n*\n/\n")

        if operation_symbol not in "+-*/":
            # Forces user to type in a valid operation without producing an error
            print("\nPlease type a valid operation")

        else:
            num2 = float(input("\nWhat is the second number?:"))
            calculation_function = operations[operation_symbol]
            answer = calculation_function(num1, num2)
            print(f"\n{num1} {operation_symbol} {num2} = {answer}")

            if input(
                    "\ntype 'y' to continue with this calculation, type 'n' to start a new calculation").lower() == "y":
                # makes the first number the answer and runs through the program again allowing the user to use
                # another operation
                num1 = answer
            else:
                # Recursively runs through the beginning of the program
                is_running = False
                calculator()


calculator()
