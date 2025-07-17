# Write a program that asks for a person's age and checks if they are 18 or older. If they are, print You are eligible to vote.

age = int(input("Your age? "))

def check_age(age):
    if age >= 18:
        return ("You are eligible to vote.")

print(check_age(age))