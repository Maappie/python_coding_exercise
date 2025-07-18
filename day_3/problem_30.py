# Write a program that asks for a person's age and checks if they are a teenager (between 13 and 19) or an adult (20 and older). 
# If they are a teenager, print You are a teenager. If they are an adult, print You are an adult. 
# If they are younger than 13, print You are a child.

age = int(input("Enter your age: "))

def check_age(par_age):
    if 13 <= par_age <= 19:
        print("You are a teenager.")
    elif par_age >= 20:
        print("You are an adult.")
    elif 0 <= par_age <= 12:
        print("You are a child.")

check_age(age)