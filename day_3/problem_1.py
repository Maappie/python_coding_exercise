# Write a program that asks the user for a number and checks if it is positive. 
# If the number is positive, print The number is positive.    

number = int(input("Enter a number: "))

def check_number(number):
    if number > 0:
        print("Number is positive")
    elif number < 0:
        print("Number is negative")
    else:
        print("Not positive or negative")
        
check_number(number)