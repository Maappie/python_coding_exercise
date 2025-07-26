# Create an array of words and print the length of each word.

fruits = ["apple", "banana", "grape"] 

def show_length(par_fruits):
    for x in range(len(par_fruits)):
        print(f"{fruits[x]} has a length of {len(fruits[x])}")
show_length(fruits)