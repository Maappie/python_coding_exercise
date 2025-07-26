# Create an array of numbers ([2, 4, 6]) and print each number doubled.

numbers = [2, 4, 6]

def show_number_doubled(par_numbers):
    for x in range(len(par_numbers)):
        print(f"{par_numbers[x] * 2}")
show_number_doubled(numbers)