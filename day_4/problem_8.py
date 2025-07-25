# Use the times method to reverse an array of strings. Print each string in reverse order of its original position.

strings = ["one", "two", "three", "four", "five"]

def show_in_reverse(par_strings):
    for x in range(len(par_strings) - 1, -1, -1):
        print(par_strings[x])

show_in_reverse(strings)