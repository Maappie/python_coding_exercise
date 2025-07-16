# You have a hash of items in a shopping cart, Remove the item "watch" from the cart and print the updated hash.

cart = { "shoes": 50, "bag": 30, "watch": 20 }

def remove_key(dictionary, key_to_remove):
    dictionary.pop(key_to_remove)
    return dictionary

print(f"Before remove: {cart}")
print(f"After remove: {remove_key(cart, "watch")}")