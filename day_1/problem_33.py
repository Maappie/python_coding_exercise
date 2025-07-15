# Ask the user to input their name and print the name with the first letter capitalized using .capitalize.

name = str(input("Enter your name: "))

def capitalize(name):
    return name.capitalize()

print(f"Your name is {capitalize(name)}")