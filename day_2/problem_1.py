# You have a list of fruits, Add the fruit "orange" to the list and print the updated list.

def add_item(item, list):
    list.append(item)    
    return list

fruits = ["apple", "banana", "cherry", "date"]

fruits = add_item("orange", fruits)

print(fruits)