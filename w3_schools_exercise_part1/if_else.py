# use if, elif, else statement to check which number is higher or if they are equal
a = 10
b = 4

if a > b:
    print("a is greater than b")
elif a < b:
    print("b is greater than b")
else:
    print("a and b are equal")

# short hand if statement
if a > b: print("a is greater than b")

# short hand if else statement
print("a is higher") if a > b else print("b is higher") 

# multiple else in if statement
print("a is higher") if a > b else print("b is higher") if a < b else print("they are equal")

# use 'and' if you want 2 conditions to be met
num1 = 10
num2 = 12
num3 = 3

if num1 > num3 and num2 > num3:
    print("num1 and num2 are higher than num3")
    
# use 'or' if you want at least one condition to be met
if num1 > num3 or num2 > num3:
    print("num1 or num2 is higher than num3")

# use 'not' if you want the opposite of the condition to be met
if not num1 > num2:
    print("num1 is not higher than num2")

# use nested if statement if you have multiple conditions to be met
if num1 > num2:
    if num2 > num3:
        print("num1 and num2 is higher than num3")
    elif num2 < num3:
        print("only num1 is higher than num3")
elif num1 < num2:
    print("num1 is lower than num2")

# use the pass statement if you have if statement that dont have content

if num1 > num2:
    pass
elif num1 > num3:
    print("num1 is greater than num3")