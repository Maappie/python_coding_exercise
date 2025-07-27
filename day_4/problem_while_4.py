# Create a program that prints the multiplication table for a number, but stops when the product exceeds 50.

num = int(input("Enter a number: "))

counter = 1
while True:
    product = num * counter
    
    if product > 50:
        break
    print(f"{num} x {counter} is: {product}")
    
    counter += 1