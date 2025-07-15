#Ask the user for a word, reverse the word and print it.

word = str(input("Enter a word: "))

def reverse_word(word):
    return word[::-1]

print(f"{reverse_word(word)}")