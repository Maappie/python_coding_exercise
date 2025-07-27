# Ask the user for a number, and use a for loop to print a right-angled triangle with that number of rows made of stars (*).

number = int(input("Enter a number: "))

def show_right_triangle(par_number):
    for x in range(par_number):
        print(f"x" * (x+1))
show_right_triangle(number)