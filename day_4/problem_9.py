# Write a Python program that asks the user for a number and prints a right-angled triangle of asterisks (*) with the given number of rows.

number = int(input("Enter a number: "))

def show_right_triangle(par_number):
    
    for x in range(par_number):
        print("x" * (x + 1))

show_right_triangle(number)