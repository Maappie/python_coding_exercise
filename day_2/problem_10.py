# You have an array of countries, Find and print the index of "Mexico".

countries = ["USA", "Canada", "Mexico", "Germany", "France"]

def find_value(list, value):
    result = list.index(value)
    return result

print(find_value(countries, "Mexico"))

