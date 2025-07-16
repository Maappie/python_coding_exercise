# Given an array, remove the first element and print the updated array.

animals = ["cat", "dog", "rabbit", "hamster"]

def remove_first_element(list):
    list.pop(0)
    return list

print(remove_first_element(animals))
    