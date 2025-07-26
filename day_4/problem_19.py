# Create a dictionary with three key-value pairs (e.g., ) and print each key and its corresponding value.

dictionary = {'a': 1, 'b': 2, 'c': 3}

def show_key_value_pair(par_dictionary):
    print(list(par_dictionary.items()))
    
show_key_value_pair(dictionary)