# Write a program that prints numbers from 1 upwards using until, and stops when it reaches a number divisible by 7. Use break to exit.

counter = 1
while True:
    if counter % 7 == 0:
        break

    print(counter)
    counter += 1