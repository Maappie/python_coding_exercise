# Create a variable for the current temperature in Celsius and convert it to Fahrenheit. Print both values.

celsius = float(input("Enter the current temperature in Celsius: "))

def calculate(celsius):
    return (celsius * (9/5)) + 32

print("The temperature is", str(celsius))
print("The fahrenheit is", calculate(celsius))