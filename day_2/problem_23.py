# Create a hash with three of your favorite books and their authors. Print the author of the second book.

books = {
    "book 1": "auth 1",
    "book 2": "auth 2",
    "book 3": "auth 3"
}

def print_value(dictionary):
    titles = list(dictionary.values())
    title = titles[1]
    return title

print(f"After fetch: {print_value(books)}")