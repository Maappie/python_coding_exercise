# Write a program that loops through an array of names and capitalizes each name. Print the updated array of capitalized names.

names = ["renz", "daenco", "barako", "maps"]

def capitalize_array(par_names):
    for item in range(len(par_names)):
        par_names[item] = par_names[item].capitalize()
    return par_names

capitalize_array(names)
print(names)