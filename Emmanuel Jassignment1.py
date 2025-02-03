# 1. Simple Calculator
# Write a simple calculator that takes two numbers and an operator (+, -, *, /) as input and returns the result of the operation.

# Psedo Code:
# 1. Take two numbers and an operator as input.
# 2. Perform the operation based on the operator.
# 3. Print the result.

def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter the operator (+, -, *, /): ")
result = calculate(num1, num2, operator)
print(f"The result is: {result}")

# 2. Area of a Rectangle
# Write a program that takes the length and width of a rectangle as input and calculates the area of the rectangle.

# Psedo Code:
# 1. Take the length and width of the rectangle as input.
# 2. Calculate the area of the rectangle.
# 3. Print the area.

def calculate_area(length, width):
    return length * width
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = calculate_area(length, width)
print(f"The area of the rectangle is: {area}")
