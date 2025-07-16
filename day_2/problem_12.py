# Given an array of numbers , reverse the array and print the result.

numbers = [3, 6, 9, 12, 15]

def reverse_array(arr):
    arr.reverse()
    return arr

print(f"Before reverse: {numbers}")
print(f"After reverse: {reverse_array(numbers)}")
 