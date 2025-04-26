# Define functions for basic arithmetic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed"

# Main function to interact with the user
def calculator():
    # Get user input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculations using functions
    print("Addition: ", add(num1, num2))
    print("Subtraction: ", subtract(num1, num2))
    print("Multiplication: ", multiply(num1, num2))
    print("Division: ", divide(num1, num2))

# Call the calculator function to execute the program
calculator()
