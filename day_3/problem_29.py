# Write a program that asks for a username and password. 
# If the username is admin and the password is secret, print Access granted. Otherwise, print Access denied.

username = str(input("Enter username: "))
password = str(input("Enter password: "))

def login(par_username, par_password):
    if par_username == "admin" and par_password == "secret":
        print("Access granted.")
    else:
        print("Access denied.")
login(username, password)