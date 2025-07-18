# Write a program that asks for a string and checks if it is empty or only contains spaces.
# If either condition is true, print The string is empty or only contains spaces. Otherwise, print The string has valid content.

word = str(input("Enter a word: "))


def check_word(par_word):
    if par_word.strip():
        print("The string has valid content:")
    else:
        print("The string is empty or only contains spaces.")

check_word(word)