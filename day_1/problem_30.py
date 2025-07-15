# Ask the user for a word, extract and print the first 5 characters.

word = str(input("Enter a word: "))

def print_five_letters(word):
    return word.replace(" ","")[:5]

print(f"Your word is {word} and the first five letters are: {print_five_letters(word)}")