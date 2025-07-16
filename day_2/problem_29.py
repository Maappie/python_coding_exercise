# Print the name of person 2

persons ={
 "person1": {"name": "Alice", "age": 30}, 
 "person2": {"name": "Bob", "age": 25}
}

def print_person(dictionary, key_reference, value_reference):
    return dictionary[key_reference][value_reference]
    
print(print_person(persons, "person2", "name"))