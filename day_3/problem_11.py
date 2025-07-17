# Write a program that asks the user for a number and checks if it is positive or negative. 
# If it is positive, print The number is positive Otherwise, print The number is negative.

number = int(input("Enter a number: "))

def check_number(number):
    if number < 0:
        print("The number is negative.")
    elif number > 0:
        print("The number is positive.")
    else:
        print("Not positive or negative")

check_number(number)