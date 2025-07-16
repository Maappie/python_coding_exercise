# You have an array of 5 items. Print each item with its index using a loop.

animals = ["cat", "dog", "rabbit", "hamster", "bird"]

def print_all_items(arr):
    for x in range(len(arr)):
        print(f"{arr[x]} is found at index {x}")

print_all_items(animals)