# Ask the user for a number and print the square root of the number.

import math 

number = float(input("Enter a number: "))

def square(number):
    return math.sqrt(number)

print(f"The square root of the number: {number} is {square(number)}")