# Write a program that asks the user to enter a password. Keep asking until the correct password ("secret") is entered.

while True:
    
    passw = str(input("Enter password:"))
    
    if passw == "secret":
        break
