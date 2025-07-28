# Write a program that prints even numbers between 1 and 50 using a while loop, but stops when the number 30 is reached. 
# Use break to exit the loop when this condition is met.

counter = 1
while 50 > counter:
    if counter % 2 == 0:
        print(counter)
    elif counter > 30:
        break
    
    counter += 1