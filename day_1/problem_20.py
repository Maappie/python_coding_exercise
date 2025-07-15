# Ask the user for their birth year, calculate how old they will be in 5 years, and print it.

birth_year = int(input("birth year?"))
base_year = 2029

def calculate(birth_year, base_year):
   return base_year - birth_year

print(calculate(birth_year, base_year))