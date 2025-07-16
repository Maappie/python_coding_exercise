# There is a hash that contains details about a car, Update the year to 2020 and print the updated hash.


car = { "maker": "Toyota", "model": "Corolla", "year": 2015 }

def update_car(dictionary, key_reference, value_to_replace):
    dictionary[key_reference] = value_to_replace
    return dictionary

print(update_car(car, "year", 2020))