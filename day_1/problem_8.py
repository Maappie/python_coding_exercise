# Create two variables: one for your birth year and one for the current year. Calculate and print your age.

def age(birth_year, current_year):
    age = current_year - birth_year
    return age


birth_year = 2004
current_year = 2025
print(age(birth_year, current_year))