# Write a program that asks the user for a number and checks if it is between 50 and 100 (inclusive) and if it is even. 
# Print The number is valid and even. if both conditions are true, otherwise print The number does not meet the criteria.

number = int(input("Enter a number: "))

def check_number(par_number):
    if 50 <= par_number <= 100 and par_number % 2 == 0:
        print("The number is valid and even.")
    else:
        print("The number does not meet the critertia.")

check_number(number)