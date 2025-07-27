# Use a for loop to print only the even numbers between 1 and 20.

def show_even_numbers():
    for x in range(20):
        if (x+1) % 2 == 0:
            print(x+1)

show_even_numbers()