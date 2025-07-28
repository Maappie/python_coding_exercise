# Write a program that repeatedly asks the user for a number and checks if it is prime. 
# Use break to exit when the user enters "exit". Use continue to skip numbers less than 2.

import math
while True:
    user_input = input("(type 'exit' to exit) Enter a number: ")
    
    if user_input == "exit":
        break

    number = int(user_input)

    if number < 2:
        continue

    is_prime = True
    for i in range(2, int(math.sqrt(number)) +1):
        if number % i == 0:
            is_prime = False
            break
    
    print("It is a prime number ") if is_prime == True else print("Not a prime number")
        
