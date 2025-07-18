# Write a program that loops through an array of numbers and replaces any negative numbers with 0. Print the updated array.

numbers = [1, 2, 3, 4, 10, -1 , -22 ,-3]

def replace_negative_numbers(par_numbers):
    for each_number in range(len(par_numbers)):
        if par_numbers[each_number] < 0:
            par_numbers[each_number] = 0
    return par_numbers

replace_negative_numbers(numbers)

print(numbers)