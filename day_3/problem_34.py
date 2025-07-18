# Write a program that loops through an array of numbers and counts how many of them are positive. Print the total count at the end.

numbers = [1, 2, 3, 4, 10, -1 , -22 ,3]

def check_for_positive(numbers):
    total_positive = 0
    for num in numbers:
        if num > 0:
            total_positive += 1
    return total_positive

print(check_for_positive(numbers))