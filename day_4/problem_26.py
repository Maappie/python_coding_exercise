# Create an array of strings and use the each method to reverse each string and print it.

import string
import random

word = "".join(random.sample(string.ascii_letters, k = 5))

def reverse_string(par_word):
    par_word = "".join(reversed(par_word))
    return par_word

print(word)
print(reverse_string(word))