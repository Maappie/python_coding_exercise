# Create an array of names and use the each method to capitalize each name and print it.

names = ["john", "jane", "doe"]

def capitalize_each_string(par_string):
    for x in range(len(par_string)):
        par_string[x] = par_string[x].capitalize()
    
    print(par_string)
capitalize_each_string(names)