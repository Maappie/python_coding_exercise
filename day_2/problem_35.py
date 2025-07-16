# Print the second red fruit.

fruits = { "red": ["apple", "cherry"], "yellow": ["banana", "lemon"]}

def print_fruit(dictionary, key_reference, index_reference):
    return dictionary[key_reference][index_reference]

print(print_fruit(fruits, "red", 1))