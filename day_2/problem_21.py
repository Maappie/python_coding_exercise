# There is a hash representing a student’s grades, Update the grade for English to 95 and print the updated hash.


grades ={ "math": 90, "english": 85, "science": 88 }

def update_grades(dictionary, key, value_to_replace):
    dictionary[key] = value_to_replace
    return dictionary
print(f"Before update: {grades}")
print(f"After update: {update_grades(grades, "english", 95)}")