# Write a program that counts how many odd numbers are in an array using a while loop and a conditional statement.

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11, 13]

i = 0
odd_count = 0
while len(array) > i:
    if array[i] % 2 != 0:
        odd_count += 1
    i += 1
    
print(odd_count)