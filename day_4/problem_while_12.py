# Write a program that checks if all elements in an array are positive numbers.

array = [1, 2, 3, 6, 4, 5, 6, 7, 8, 9, 10, 12, 11, 13]

counter = 0

while len(array) > counter:
    if array[counter] < 1:
        print("Not all numbers are positive")
    elif len(array) == counter + 1:
        print("All numbers are Positive")
    counter += 1
