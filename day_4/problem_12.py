# Ask the user for a number and print a pyramid pattern of numbers. For example, for input 5:
    # 1
    # 22
    # 333
    # 4444
    # 55555
    
number = int(input("Enter a number: "))

def generate_pattern(par_number):
    for x in range(par_number):
        print(f"{(x+1)}" * (x+1))

generate_pattern(number)
