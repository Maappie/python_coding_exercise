# append method is to add an item at the end of list
list = ["hotdog", "burger", "salad"]
print(f"Before append: {list}")
list.append("sandwich")
print(f"After append: {list}\n")

# insert method is to add an item in the specified index
list = ["hotdog", "burger", "salad"]
print(f"Before insert: {list}")
list.insert(1,"sandwich")
print(f"After insert: {list}\n")

# extend method is to append the elements of list A to list B
list_one = ["hotdog", "burger", "salad"]
list_two = ["coke", "pepsi", "royal"]
print(f"Before extend: {list_one} {list_two}")
list_one.extend(list_two)
print(f"After extend: {list_one}\n")

# extend does not only combine 2 lists, you can also add other types of collections
list_one = ["hotdog", "burger", "salad"]
list_two = {"coke", "pepsi", "royal"} # this is a collection type 'set'
print(f"Before extend: {list_one} {list_two}")
list_one.extend(list_two)
print(f"After extend: {list_one}")

