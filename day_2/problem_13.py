# Create an array with five different animals. Replace the third animal with "tiger" and print the updated array.

animals = ["cat", "dog", "rabbit", "hamster", "bird"]

def replace_item(arr, replace_with):
    arr = [item if i != 2 else replace_with for i, item in enumerate(arr)]
    return arr

print(f"Before update: {animals}")
print(f"After update: {replace_item(animals, "tiger")}")

