# Write a program that takes two numbers and checks if they are equal. 
# If they are equal, print The numbers are equal. Otherwise, print The numbers are not equal.

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

def compare_numbers(num1, num2):
    if num1 == num2:
        print("The numbers are equal.")
    else:
        print("The numbers are not equal.")

compare_numbers(num1, num2)