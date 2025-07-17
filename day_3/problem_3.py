# Write a program that takes two numbers and checks if they are equal.
# If they are, print The numbers are equal.

num1 = int(input("enter a number: "))
num2 = int(input("enter a number: "))

def compare_numbers(num1, num2):
    if num1 == num2:
        return ("The numbers are equal")
    return ("")

print(compare_numbers(num1, num2))