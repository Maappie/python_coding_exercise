# Create a dictionary to represent a library book with the following information: title is "koda", author is "mark", and pages is 100. Print the book's title.

def create_book():
    book = {
        "title": "koda",
        "author": "mark",
        "page": 100
    }
    return book
    
print(f"The book title is {create_book()["title"]}")