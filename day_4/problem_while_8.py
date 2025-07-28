# Write a program that goes through an array and creates a new array containing only even numbers using a while loop.

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_array = []

i = 0
while len(array) > i:
    print(i)
    if array[i] % 2 == 0:
        new_array.append(array[i])
    i += 1
    
print(new_array)