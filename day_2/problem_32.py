# Print the model of car1

cars = dict(
        car1 = dict(make= "Toyota", model= "Corolla"), 
        car2 = dict(make= "Ford", model= "Mustang")
        )
def print_car(dictionary, key_reference, inner_key_reference):
    result = dictionary[key_reference][inner_key_reference]
    return result

print(print_car(cars, "car1", "model"))