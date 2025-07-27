# Create two arrays, one with keys and one with values, and use the each method to combine them into a dictionary.

key_names = ["house", "car", "pool"]
value = [200, 150, 250]

def create_ditionary(par_key_names, par_value):
    par_key_names = dict(zip(par_key_names, par_value))
    return par_key_names

new_dictionary = create_ditionary(key_names, value)

print(new_dictionary)    
