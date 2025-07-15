# Ask the user for a number and print the square of the number.

number = float(input("Enter a number: "))

def square(number):
    return number * number

print(f"The square of the number: {number} is {square(number)}")