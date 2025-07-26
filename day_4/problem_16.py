# Create an array of numbers and use the each method to print each number.

numbers = [1, 2, 3, 4, 5] 

def show_numbers():
    for x in range(len(numbers)):
        print(numbers[x], end = " ")
show_numbers()