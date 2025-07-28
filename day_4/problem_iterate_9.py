# Write a program that asks the user to enter numbers and adds them to a total. 
# If the number is divisible by 4, it skips adding it using next. The loop stops when the total exceeds 50.

total = 0
while True:
    
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Enter a valid number")
        continue
    
    if num % 4 == 0:
        continue
    total += num
    if total > 50:
        break


print(total)
    
        