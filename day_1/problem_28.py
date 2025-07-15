# Ask the user to input a word and print the length of the word using the .length method.

word = str(input("Enter a word: "))

def word_length(word):
    return len(word.replace(" ",""))

print(f"The {word} has a length of {word_length(word)}")
