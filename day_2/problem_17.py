# Create an array of five random numbers. Add two more numbers to the beginning of the array and print the updated array.

numbers = [1, 2, 3, 4, 5]

def add_number(list, to_add, to_add2):
    list = [to_add, to_add2] + list
    return list

print(f"Before add: {numbers}")
print(f"After add: {add_number(numbers, 10, 20)}")