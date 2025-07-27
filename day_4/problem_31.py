# Use a for loop to calculate and print the sum of all numbers from 1 to 100.

def sum_numbers():
    result = 0
    for x in range(100):
        result += x
    return result

print(sum_numbers())