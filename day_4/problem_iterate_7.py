# Write a program that prints numbers from 1 to 20, skipping multiples of 5 using continue. Use an while not loop to stop once the number exceeds 20.

counter = 1
while not counter > 20:
    if counter % 5 != 0:
        print(counter)
    else:
        counter += 1
        continue
    counter += 1