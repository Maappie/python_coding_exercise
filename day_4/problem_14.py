# Create a Python program that generates a random string of 8 characters, 
# where each character is randomly chosen from a set of lowercase letters a to z

import string
import random

lowercase_letters = string.ascii_lowercase

def generate_string(): 
    word = "".join(random.sample(lowercase_letters, k =  8 ))
    print(word)
    
generate_string()