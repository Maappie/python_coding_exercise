# Use a for loop to print the multiplication table of 5.

def show_multiplication_table():
    for x in range(10):
        print(f"{x+1} x 5 is {(x+1) * 5}.")

show_multiplication_table()