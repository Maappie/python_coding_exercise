# Concatenate the first three characters of a string with the last two characters of another string and print the result.

def concat_strings(str1, str2):
    return str1[:3] + str2[-2:]

# Example usage:
first = input("Enter the first string: ")
second = input("Enter the second string: ")

result = concat_strings(first, second)
print(result)
