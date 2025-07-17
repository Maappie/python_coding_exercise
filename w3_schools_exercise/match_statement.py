# match is like a case statement in c++, where if you have many conditions you can use match instead
# case _ is default or like else, if no condition is met then it falls to the default
person = 4
match person:
    case 0:
        print("there are no persons")
    case 1:
        print("there is only 1 person")
    case 2:
        print("theer are 2 persons")
    case _:
        print("I dont know how many are there")
    
# combine values is like an or statement

match person:
    case 1 | 2 | 3:
        print("there are persons")
    case 0:
        print("there are no person")
    case _:
        print("I dont know")
        
# if statements as guaurds, it is like having two different conition is two criterta

age = 21
year = 2004

match 21:
    case 1 | 2 | 3 if year > 2000:
        print("You are too young")
    case 21 if year == 2004:
        print("You are a young adult ")
    case _:
        print("I dont know")