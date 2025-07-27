# Create an array of words and  to check if each word is a palindrome (a word that reads the same backward as forward).

words = ["ate", "aba", "human", "ata", "daad"]

def palindrome_checker(par_words):
    palindromes = []
    for word in par_words:
        if word == word[::-1]:
            palindromes.append(word)
    return palindromes
print(palindrome_checker(words))
