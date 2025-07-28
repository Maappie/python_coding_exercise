# Write a program that prints all even numbers from 1 to 20 using a while loop.

number = 20
def add_all_even_numbers(par_num, counter = 1 ):
    while counter <= par_num:
        if counter % 2 == 0:
            print(counter)
        counter += 1
    
add_all_even_numbers(number)
