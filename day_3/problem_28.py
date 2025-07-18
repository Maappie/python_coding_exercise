# Write a program that asks for a number and checks whether it is positive, negative, or zero. Print The number is positive. 
# if it’s positive, The number is negative. if it’s negative, or The number is zero. if it's zero.

number = int(input("Enter a number: "))

def check_number(par_number):
    if par_number > 0:
        print("The number is positive.")
    elif par_number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")
        
check_number(number)