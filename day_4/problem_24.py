# Create two arrays of equal length and use the each method to multiply corresponding elements from each array and print the results.

import string
import random

array_one = random.sample(string.digits, k = 6)
array_one_int = [int(number) for number in array_one]

array_two = random.sample(string.digits, k = 6)
array_two_int = [int(number) for number in array_two]

def multiply_arrays(par_array_one, par_array_two):
    new_array = []
    for number in range(len(par_array_one)):
        new_array.append(par_array_one[number] * par_array_two[number])
    return new_array
        

print(f"This is array one: {array_one_int}")
print(f"This is array two: {array_two_int}")
print(f"This is multiplied array: {multiply_arrays(array_one_int, array_two_int)}")
