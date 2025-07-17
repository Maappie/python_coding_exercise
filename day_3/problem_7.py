# Write a program that asks the user for two words and checks if they are the same. 
# If the two words are the same, print The words are identical.

word_1 = str(input("Enter the first word: "))
word_2 = str(input("Enter the second word: "))

def compare_words(word_1, word_2):
    if word_1 == word_2:
        print("The words are identical")

compare_words(word_1, word_2)