# list is like an array *ordered, changeable, indexed. Allows duplicate.
list_of_fruits = ["apple", "banana", "pear", "mango"]
print(list_of_fruits)
print(list_of_fruits[1:-1])
print(len(list_of_fruits))

# list with different data type have a data type 'list'
list1 = ["abc", 34, True, 40, "male"]
print(type(list1))
print(type(list[0]))

# use 'list' constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# use tuple to create array and it uses parenthesis unlike list uses bracket *ordered and immutable or the values are unchangable after creation. Can duplicate*
movies = ("movie 1", "movie 2", "movie 3")
print(movies)

# use set to create array and this uses curly brackets *unordered, immutable, and unindexed. No duplicate*
my_set = {"Renz", 21, "Manila"}

print(my_set)

# Creating a dictionary with some key-value pairs
student_info = {
    "name": "Renz",
    "age": 21,
    "city": "Manila"
}
print(student_info)
