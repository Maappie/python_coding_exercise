# Ask the user for a number and use the times method to print "This is iteration number X" for each iteration, where X is the current iteration number.

number = int(input("Enter a number: "))

def iteration():
    for x in range(number):
        print(f"This is iteration number {x+1}") 

iteration()
    