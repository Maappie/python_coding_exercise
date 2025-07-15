# Print the result of dividing 50 by a variable, then print the remainder using modulo.

divisor = float(input("Enter a number: "))

def calculate(divisor):
    result = 50 % divisor
    return result

print("The remainder is", f"{calculate(divisor):.2f}")