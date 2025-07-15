# Start with 64, divide it by 8 using the /= operator, and print the final result.

def divide_value(number, divided_by):
    number /= divided_by
    return number

print(divide_value(64, 8))