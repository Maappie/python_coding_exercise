# use remove method to delete a specified item *only remove the first occurence if there is a duplicate*
list = ["hotdog", "burger", "salad", "hotdog"]
print(f"Before remove: {list}")
list.remove("hotdog")
print(f"After remove: {list}\n")

# use pop to delete the specified index *by default it will pop the last if index is not specified*
list = ["hotdog", "burger", "salad", "hotdog"]
print(f"Before remove: {list}")
list.pop(1)
print(f"After remove: {list}\n")

# del method also deletes item from the specified index or delelte whole list
list = ["hotdog", "burger", "salad", "hotdog"]
print(f"Before delete: {list}")
del list[2] 
print(f"After delete(index): {list}")
del list
print(f"After delete(whole): {list}\n")

# clear method will delete all items or empty out the list
list = ["hotdog", "burger", "salad", "hotdog"]
print(f"Before delete: {list}")
list.clear() 
print(f"After delete(index): {list}")