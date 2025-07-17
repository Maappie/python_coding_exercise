# Write a program that asks for a word and checks if it contains the letter a.
# If it does, print The word contains the letter 'a'.

word = str(input("Enter a word: "))

def check_word(word):
    word_with_a = [each_word for each_word in word.split() if 'a' in each_word]
    return word_with_a

word_with_a = check_word(word)

if word_with_a:
    for with_a in word_with_a:
        print(f"The word: {with_a}, contains the lettea 'a'")
else:
    print("No word with 'a' found")