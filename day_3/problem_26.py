# Write a program that asks for the user’s age and whether they have passed the driving test. 
# If they are at least 18 and have passed the test, print You are eligible for a driver's license. 
# Otherwise, print You are not eligible.

age = int(input("Enter you age: "))
passed = bool(int(input("Enter '1' if you passed the driving test, '0' if not. ")))

def check_eligibility(par_age, par_passed):
    if par_age >= 18 and par_passed == True:
        return ("You are eligiblle for a driver's license.")
    else:
        return ("You are not eligible.")
    
print(check_eligibility(age, passed))