# Write a program that asks for a person's age and checks if they are 65 or older. 
# If they are, print You are a senior citizen. Otherwise, print You are not a senior citizen.

age = int(input("Enter your age: "))

def check_age(par_age):
    if par_age >= 65:
        print("You are a senior citizen. ")
    else:
        print("You are not a senior citizen. ")

check_age(age)