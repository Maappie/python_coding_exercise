# You are given an array of numbers, Remove the last number from the array and print the result.

def remove_last_number(list):
    list.pop()
    return list

numbers = [10, 20, 30, 40, 50]

numbers = remove_last_number(numbers)

print(numbers)