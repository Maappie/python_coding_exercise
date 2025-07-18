# Write a program that loops through an array of numbers and prints All numbers are greater than 10 if every number is greater than 10.

numbers = [12, 22, 31, 14, 15, 16, 12, 13, 12, 45]

def check_numbers(par_numbers):
    result = True
    for item in range(len(par_numbers)):
        if par_numbers[item] <= 10:
            result = False
            return result
    return result
result = check_numbers(numbers)
print("All numbers are greater than 10") if result == True else print("")