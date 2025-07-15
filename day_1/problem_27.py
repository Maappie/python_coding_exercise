# Create a variable for the price of two items, calculate the total, and print it with a message like “The total is [total].”

item_1 = 15.63
item_2= 12.25

def add_items(item1, item2):
    return item1 + item2 

print("Your total is", f"{add_items(item_1, item_2):.2f}")

