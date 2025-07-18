# Write a program that asks for a person's age and checks if they are 18 or older. 
# If they are, print You are eligible to vote. Otherwise, print You are not eligible to vote.

age = int(input("Enter your age: "))

def check_age(age):
    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible to vote.")

check_age(age)