# Write a program that asks the user for two words and checks if they are the same. 
# If they are the same, print The words are identical. Otherwise, print The words are different.

word1 = str(input("Enter the first word: "))
word2 = str(input("Enter the second word: "))

def check_words(c_word1, c_word2):
    if c_word1 == c_word2:
        print("The words are identical.")
    else:
        print("The words are different.")

check_words(word1, word2)