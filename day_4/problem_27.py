# Create a string and use the for method on the characters of the string to count the occurrences of each letter,
# storing the results in a dictionary

import string
import random

word = "".join(random.choices(string.ascii_lowercase, k = 10))
letter_counts = {}

def check_occurences(par_word):
    for char in par_word:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1

print(word)
check_occurences(word)
print(letter_counts)
