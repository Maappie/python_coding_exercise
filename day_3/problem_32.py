# Write a program that loops through an array of numbers and sums all the odd numbers. Print the total sum at the end.

numbers = [1 ,2 ,3, 4, 5]

def show_even_numbers(par_numbers):
    result = 0
    for num in par_numbers:
        if not num % 2 == 0:
            result += num
    return result

print(show_even_numbers(numbers))