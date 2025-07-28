# Write a program that repeatedly asks the user for a password until they enter "python123". 
# Use break to exit the loop once the correct password is entered.

while True:
    passw = input("Enter password: ")
    
    if passw == "python123":
        break
    else:
        continue