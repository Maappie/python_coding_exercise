# Create an array of words and use a for loop to print each word in reverse.

words = ["giant", "tree", "milk", "mappie"]

def show_in_reverse(par_words):
    for word in par_words:
        print(word[::-1])
show_in_reverse(words)