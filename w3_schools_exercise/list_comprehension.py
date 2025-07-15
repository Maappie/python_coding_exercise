# create new list but only those with "a"
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
        
print(f"Original list: {fruits}")
print(f"New list: {newlist}\n")

# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
# syntax is read as newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [i for i in fruits if "a" in i]

print(f"Original list: {fruits}")
print(f"New list: {newlist}\n")

# or if you want the full list then. newlist = [x for x in fruits]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(f"Original list: {fruits}")
print(f"New list: {newlist}\n")

# or you can use range method *if condition is optional*
newlist = [x for x in range(10) if x < 5]
print(newlist, "\n")

# replaces items that met the condition from the list with the specified value or item (in this case, replace the items from the list 'fruits' if there is 'a' by 'menudo')
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "potato"]
newlist = ['menudo' for x in fruits if "a" in x]
print(newlist, "\n")

fruits = ["apple", "banana", "cherry", "kiwi", "mango", "potato"]
print(fruits)
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist, "\n")



