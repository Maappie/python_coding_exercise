# You have an array of numbers: . Combine all numbers into a string, separated by hyphens ("-"), and print the result.


numbers = [100, 200, 300, 400, 500]

def list_to_string(list):
    list = '-'.join(str(number) for number in list)
    return list

print(f"Before combining items: {numbers}")

print(f"After combining items: {list_to_string(numbers)}")