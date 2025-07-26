# Create an array of numbers and use the each method to calculate the sum of all elements in the array.

numbers = [1, 2, 3, 4, 5, 6, 10]

def add_numbers(par_numbers):
    result = 0
    for x in range(len(par_numbers)):
        result += par_numbers[x]
    return result
print(add_numbers(numbers))
