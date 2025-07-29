# using add or + to join 2 list
names = ["renz", "sam", "habla", "sean"]
names_two = ["jris", "jafet","felix"]

joined_list = names + names_two
print(joined_list)

# using append to join 2 list
names = ["renz", "sam", "habla", "sean"]
names_two = ["jris", "jafet","felix"]

for x in names_two:
    names.append(x)

print(names)

# using extend method 
names = ["renz", "sam", "habla", "sean"]
names_two = ["jris", "jafet","felix"]

names.extend(names_two)

print(names)