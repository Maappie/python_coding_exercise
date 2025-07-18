# Write a program that loops through an array of numbers and finds the largest number. Print the largest number at the end.

numbers = [1, 3, 4, 5, 6, 12, 21, 23, 5, 100]

def check_highest_number(par_numbers):
    result = max(par_numbers)
    return result

print(check_highest_number(numbers))