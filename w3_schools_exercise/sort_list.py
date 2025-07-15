# sort using the sort method (ascending)
numbers = [20, 13, 1, 3, 23, 43, 10]
print(f"Before sort: {numbers}")
numbers.sort()
print(f"After sort: {numbers}\n")

# sort using the sort method (descending)
numbers = [20, 13, 1, 3, 23, 43, 10]
print(f"Before sort: {numbers}")
numbers.sort(reverse=True)
print(f"After sort: {numbers}\n")

# sort by closeness to 25
def sort_function(n):
  return abs(n - 25)

numbers = [20, 13, 1, 3, 23, 43, 10]
numbers.sort(key = sort_function)
print(numbers, "\n")

# sort (case insensitive)
fruits = [ "Orange", "Kiwi", "cherry", "orange", "kiwi", "banana"]
print(f"Before sort: {fruits}")
fruits.sort()
print(f"After sort(case sensitive): {fruits}")
fruits.sort(key = str.lower)
print(f"After sort(case insensitive): {fruits}\n")

# sort by reversing with reverse method
fruits = [ "Orange", "Kiwi", "cherry", "orange", "kiwi", "banana"]
print(f"Before sort: {fruits}")
fruits.reverse()
print(f"After sort: {fruits}")
