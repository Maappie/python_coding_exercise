# You have a dictionary that stores the prices of different fruits: . Add a new fruit "orange" with a price of 4 and print the updated hash.

fruits_price = { 
          "apple": 2, 
          "banana": 1, 
          "cherry": 3 
          }

def add_item(dictionary):
    dictionary["orange"] = 4
    return dictionary

print(f"Before update: {fruits_price}")
add_item(fruits_price)
print(f"After update: {fruits_price}")

