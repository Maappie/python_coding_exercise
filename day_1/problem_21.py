# Ask the user to input their height in centimeters, convert it to meters, and print the result.

height = float(input("Height in centimeters: "))

def convert_to_meters(height):
    meters = height/100
    return meters

print(convert_to_meters(height), "meters")