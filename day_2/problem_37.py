# Create an array of dictionaries to represent students. 
# Each dictionary should contain the following keys: "name", "age" and "grade", Print the name of the 10th student

students = [
    {"name": "Alice", "age": 20, "grade": "A"},
    {"name": "Bob", "age": 21, "grade": "B"},
    {"name": "Carol", "age": 22, "grade": "C"},
    {"name": "Dan", "age": 23, "grade": "A"},
    {"name": "Eve", "age": 24, "grade": "B"},
    {"name": "Frank", "age": 25, "grade": "C"},
    {"name": "Grace", "age": 26, "grade": "A"},
    {"name": "Heidi", "age": 27, "grade": "B"},
    {"name": "Ivan", "age": 28, "grade": "C"},
    {"name": "Judy", "age": 29, "grade": "A"}  
]

def show_name(collection, index_reference, key_reference):
    return collection[index_reference][key_reference]

print(show_name(students, 9, "name"))

