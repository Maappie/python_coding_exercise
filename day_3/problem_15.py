# Write a program that asks for a word and checks if the word has more than 5 characters. 
# If it does, print The word is long. Otherwise, print The word is short.

word = str(input("Enter a word: "))

def check_word_length(word):
    if len(word) > 5:
        print("The word is long.")
    else:
        print("The word is short.")

check_word_length(word)