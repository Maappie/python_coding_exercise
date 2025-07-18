# Write a program that loops through an array of strings and prints only the strings that are longer than 4 characters.

names = ["renz", "daenco", "barako", "maps"]

def print_names(par_names):
    for item in par_names:
        if len(item) > 4:
            print(item)

print_names(names)