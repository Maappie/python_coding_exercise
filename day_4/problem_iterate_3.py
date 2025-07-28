# Write a guessing game where the computer picks a random number between 1 and 10. 
# The user must guess the number, and the program will give hints ("Too high" or "Too low").
# Use break to stop the loop when the correct guess is made.

import random

random_number = random.randint(1,10)

while True:
    guessed_number = int(input("Enter a number: "))
    
    if random_number > guessed_number:
        print("Too low")
    elif random_number < guessed_number:
        print("Too high")
    else:
        print("Guessed correctly")
        break