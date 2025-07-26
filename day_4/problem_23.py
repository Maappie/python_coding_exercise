# Create an array of numbers and use the each method to print only the even numbers.

import string
import random

numbers = random.sample(string.digits, k = 5)

numbers_int =[int(x) for x in numbers]
def show_even_numbers(par_numbers):
    result = []
    for number in par_numbers:
        if number % 2 == 0:
            result.append(number)
    return result

print(f"The numbers are {numbers_int}")
print(f"The even numbers are: {show_even_numbers(numbers_int)}")