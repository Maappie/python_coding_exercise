 # Write a program where the computer picks a random number between 1 and 100, and the user has to guess it.
 # Keep asking until they guess correctly.

import random

random_number = random.randint(1,100)
print(random_number)
while True:
    try:
        guess_number = int(input("Enter your guess number: "))
    except ValueError:
        continue
    if guess_number == random_number:
        break