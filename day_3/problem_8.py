# Write a program that asks for a number and checks if it is divisible by 5.
# If it is, print The number is a multiple of 5.

number = int(input("Enter a number: "))

def check_number(number):
    number = number % 5
    if number == 0:
        print("The number is a multiple of 5.")

check_number(number)
