# Create a dictionary with three key-value pairs (e.g., ) and use a for loop to print each key and value.

dictionary = {"name": "Alice", "age": 25, "city": "New York"}

def show_dictionary(par_dictionary):
    for x in par_dictionary:
        print(x, par_dictionary[x])

show_dictionary(dictionary)

