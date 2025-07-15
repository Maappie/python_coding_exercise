# Ask the user to input two numbers, multiply them, and print the result.

num1 = float(input("first number: "))
num2 = float(input("second number: "))

def multiply(num1, num2):
    return num1 * num2

print(f"{multiply(num1, num2):.2f}")