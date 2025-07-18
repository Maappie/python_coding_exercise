# Write a program that asks the user for a number and checks if it is even or odd. 
# If it’s even, print The number is even. Otherwise, print The number is odd.

number = int(input("Enter a number: "))

def check_if_odd_even(number):
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")

check_if_odd_even(number)