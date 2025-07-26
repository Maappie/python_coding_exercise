# Use the for method to simulate rolling two dice 10 times. After each roll, print both numbers and whether their sum is odd or even.

import random

def roll_dice():
    for x in range(10):
        number_one = random.randint(1, 6)
        number_two = random.randint(1, 6)
        print(f"{number_one}, {number_two}: ", end = "")
        odd_or_even(number_one, number_two)

def odd_or_even(par_number_one, par_number_two):
    par_number_one += par_number_two
    if par_number_one % 2 == 0:
        print("Their sum is even.")
    else:
        print("Their sum is odd.")

roll_dice()