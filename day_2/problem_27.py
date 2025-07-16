# Print all the values in the hash.


colors = { "red": "#FF0000", "green": "#00FF00", "blue": "#0000FF" }

def print_all_values(dictionary):
    return list(dictionary.values())

print(print_all_values(colors))