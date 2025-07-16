# Given an array [1, 2, 3, 4, 5, 3], remove any duplicate elements (if there are any) and print the unique values.

numbers = [1, 2, 3, 4, 5, 3]

def remove_duplicate(arr):
    unique_list = list(set(arr))
    return unique_list

print(f"Before duplicate remove: {numbers}")
print(f"After duplicate remove: {remove_duplicate(numbers)}")


