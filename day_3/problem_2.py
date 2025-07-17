# Write a program that asks the user for a number and checks if it is even. If the number is even, print The number is even.

number = int(input("Enter a number: "))

def check_if_even(number):
    number = number % 2
    return number

number = check_if_even(number)
if number == 0:
        print("The number is even.")

    
