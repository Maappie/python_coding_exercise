# Write a program that asks the user for a number and checks if it is between 10 and 20 (inclusive). 
# If it is, print The number is between 10 and 20.

number = int(input("Enter a number: "))

def check_number(number):
    if 10 <= number <= 20:
        print(f"The number is: {number}")

check_number(number)