# Write a program that asks for a number and checks if it is divisible by 3 and/or 5.
# If divisible by both, print The number is divisible by both 3 and 5.
# If only divisible by 3, print The number is divisible by 3.
# If only divisible by 5, print The number is divisible by 5.
# Otherwise, print the number is not divisible by 3 or 5.

number = int(input("Ente a number: "))

def check_match(par_number):
    match par_number:
        case _ if par_number % 3 == 0 and par_number % 5 == 0:
            print("The number is divisible by both 3 and 5.")
        case _ if par_number % 3 == 0:
            print("The number is divisible by 3.")
        case _ if par_number % 5 == 0:
            print("The number is divisible by 5.")
        case _ if not par_number % 3 == 0 and not par_number % 5 == 0:
            print("The number is not divisible by 3 or 5.")

check_match(number)
        
