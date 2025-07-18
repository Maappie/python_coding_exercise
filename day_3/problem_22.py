# Write a program that asks the user for their age and membership status. 
# If the person is a member or they are older than 60, print You are eligible for a discount. Otherwise, print You are not eligible for a discount.

age = int(input("Enter youre age: "))
membership = str(input("Enter 'yes' if you are a member and 'no' if not: "))

def check_status(par_age, par_membership):
    if par_age > 60 and par_membership == "yes":
        print("You are eligible for a discount.")
    else:
        print("You are not eligible for a desicount.")
        
check_status(age, membership)