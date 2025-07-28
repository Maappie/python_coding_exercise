# Write a program that prints all odd numbers between 1 and 20 using a while loop. Use continue to skip even numbers.

counter = 1
while counter <= 20:
    if counter % 2 == 0:
        counter += 1
        continue
    print(counter)
    counter += 1
