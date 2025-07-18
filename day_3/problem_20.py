# Write a program that asks for a number and checks if it is divisible by 10. 
# If it is, print The number is a multiple of 10. Otherwise, print The number is not a multiple of 10.

number = int(input("Enter a number: "))

def check_number(par_number):
    if par_number % 10 == 0:
        print("The number is a multiple of 10.")
    else:
        print("The number is not a multiple of 10.")

check_number(number)

