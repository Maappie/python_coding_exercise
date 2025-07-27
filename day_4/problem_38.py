# Create an array of numbers and use a for loop to calculate the sum of all even numbers in the array.

import string

numbers = [int(num) for num in string.digits]

def add_all_even(par_numbers):
    result = 0
    for x in par_numbers:
        if x % 2 == 0:
            result += x
    return result
print(numbers)
print(add_all_even(numbers))