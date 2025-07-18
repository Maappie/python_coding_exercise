# Write a program that asks the user for their age and whether they are on the guest list. 
# If they are older than 18 and on the guest list, print You can enter the club. Otherwise, print You cannot enter.

age = int(input("Age? "))
guest = bool(int(input("Ente '1' if you are a guest and '0' if not. ")))

def check_info(par_age, par_guest):
    if par_age > 18 and par_guest == True:
        print("You can enter the club. ")
    else:
        print("You cannot enter.")

check_info(age, guest)