# You are given an array of letters: ["a", "b", "c", "d", "e"]. print "f is found" if the letter "f" is in the array

letters = ["a", "b", "c", "d", "e"]

def print_value(list, to_print):
        if to_print in list:
            print(f"{to_print} is found")
        else:
            print(f"{to_print} not found")

print_value(letters, "f")