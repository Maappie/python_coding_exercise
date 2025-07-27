# Create an array of numbers and use a for loop to find and print both the maximum and minimum numbers in the array.

numbers = [13, 3 ,4 ,6 ,7 ,82, 32, 3]

def check_max_min(par_numbers):
    max_num = par_numbers[0]
    min_num = par_numbers[0]
    for x in par_numbers:
        if x > max_num:
            max_num = x
        if x < min_num:
            min_num = x   
    print(f"Array: {par_numbers}")     
    print(f"Max number is: {max_num} \nMin number is: {min_num}")

check_max_min(numbers)