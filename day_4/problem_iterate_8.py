# Write a program that squares numbers starting from 1 and prints them, but stops when the square exceeds 1000. 
# Use a loop and break when the condition is met.

counter = 1
while True:
    
    result = counter * counter
    
    if result > 1000:
        break
    
    print(result)
    counter += 1