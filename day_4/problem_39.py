# Ask the user for a string and use a for loop to count how many vowels (a, e, i, o, u) are in the string.

word = str(input("Enter a word: "))

def check_vowels(par_word):
    vowel_count = sum(1 for char in par_word.lower() if char in "aeiou")
    print(vowel_count)
    
check_vowels(word)