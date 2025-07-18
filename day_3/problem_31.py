# Write a program that loops through an array of numbers and prints each number if it is even.

numbers = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8]

def show_even_numbers(par_numbers):
    for num in par_numbers:
        if num % 2 == 0:
            print(num)

show_even_numbers(numbers)