# Create a program that asks the user for a number and then calculate and print the factorial of that number.

num = int(input("Enter a number: "))


def calculate_factorial(par_num):
    result = 1
    for x in range(par_num, 0, -1):
        result *= x 
        
    print(result)
    
calculate_factorial(num)