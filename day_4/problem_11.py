# Write a Python program that prints a series of random numbers between 1 and 100, repeating 10 times.
import random

def generate_random_number():
    for x in range(10):
        print(random.randint(1, 100), end = ", ")

generate_random_number()
