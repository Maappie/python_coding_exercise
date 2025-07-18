# Write a program that asks for a word and checks if it contains more than 7 characters and contains the letter e.
# If both are true, print The word is long and contains 'e'. Otherwise, print The word does not meet the criteria.


word = str(input("Enter a word: "))

def check_word(par_word):
    if len(par_word) > 7 and 'e' in par_word:
        print("The word is long and contains 'e'.")
    else:
        print("The word does not meet the criteria.")

check_word(word)