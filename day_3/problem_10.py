# Write a program that asks for a person's age and checks if they are a teenager (between 13 and 19). 
# If they are, print You are a teenager.

age = int(input("Enter your age: "))

def check_age(age):
    if 13 <= age <= 19:
        print("You are a teenager. ")

check_age(age)