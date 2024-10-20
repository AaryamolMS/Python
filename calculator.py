# Function definitions for basic operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Cannot divide by zero"

def power(num1, num2):
    return num1 ** num2

# Function that acts as the calculator
def calculator(num1, operator, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    elif operator == "^":
        return power(num1, num2)
    else:
        return "Invalid operator"

# Taking input from the user
num1 = float(input("Enter the first number: "))
operator = input("Enter the operator (+, -, *, /, ^): ")
num2 = float(input("Enter the second number: "))

# Calling the calculator function and printing the result
result = calculator(num1, operator, num2)
print("The result is:", result)
