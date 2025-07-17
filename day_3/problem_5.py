# Write a program that asks for a word and checks if it contains the letter a.
# If it does, print The word contains the letter 'a'.

word = str(input("Enter a word: "))

def check_the_word(word):
    word_with_a = [with_a for with_a in word.split() if 'a' in with_a]
    return word_with_a

word = check_the_word(word)

if word:
    for each_word in word:
        print(f"The word {each_word} have letter 'a'.")
else:
    print("There is no letter 'a' found.")
