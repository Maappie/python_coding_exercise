# Write a program that asks the user for numbers and adds them until the user enters 0. Display the total sum.

total = 0
while True:

    try:
        num = int(input("Enter a number: "))
    except ValueError:
        continue
        
    if num == 0:
        break
    total += num

print(total)