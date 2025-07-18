# Write a program that asks the user for a number and checks if it is between 10 and 20 (inclusive). 
# If it is, print The number is within range. Otherwise, print The number is out of range.

number = int(input("Enter a number: "))

def check_number(num):
    if 10 <= num <= 20:
        print("The number is within range.")
    else:
        print("The number is out of range.")

check_number(number)

