# Write a program that finds the index of the first occurrence of a number in an array using a while loop.

array = [1, 2, 3, 6, 4, 5, 6, 7, 8, 9, 10, 12, 11, 13]

number = 6

counter = 0
while len(array) > counter:
    if number == array[counter]:
        print(f"Number {number} is found at index {counter}")
        break
    counter += 1
