# Write a program that removes all elements greater than 10 from an array using a while loop.

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11, 13]

i = 0
while len(array) > i:
    if array[i] > 10:
        array.pop(i)
    else:
        i += 1
print(array)