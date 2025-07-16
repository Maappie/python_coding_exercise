# Add a new key-value pair for "job" with the value "developer" and print the updated hash.

info = { "name": "John", "age": 25, "city": "New York" }

def add_key_value(dictionary, key_to_add, value_to_add):
    dictionary[key_to_add] = value_to_add
    return dictionary

add_key_value(info, "job", "developer")

print(info)