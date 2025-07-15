# Ask the user to input a number and print its square (the number multiplied by itself).

number = float(input("Enter a number: "))

def calcute(number):
    return number * number

print(f"{calcute(number):.2f}", "is the square of", str(number) )