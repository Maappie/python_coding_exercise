# You have two arrays: ["red", "green", "blue"] and ["yellow", "purple", "pink"]. Combine them into one array and print the result.

color_set_one = ["red", "green", "blue"] 
color_set_two = ["yellow", "purple", "pink"]

def combine_list(arr_one, arr_two):
    arr_one.extend(arr_two)
    return arr_one

print(combine_list(color_set_one, color_set_two))