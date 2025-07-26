# Create an array of numbers and use the each method to add 2 to each number and print the result.

numbers = [1, 2, 3, 4, 5] 

def add_numbers(par_numbers):
    for x in range(len(par_numbers)):
        par_numbers[x] += 2
    return par_numbers

print(f"Before add: {numbers}")
print(f"After add: {add_numbers(numbers)}")

