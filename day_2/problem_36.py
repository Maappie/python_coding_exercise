# Print the second product from Store 2.

shops = {
    "store_1": { "products": ["apples", "oranges"]}, 
    "store_2": { "products": ["bananas", "grapes"]}
}

def show_product(dictionary, key_reference, inner_key_reference, index_reference):
    return dictionary[key_reference][inner_key_reference][index_reference]

print(show_product(shops, "store_2", "products", 1))
