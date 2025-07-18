# Write a program that loops through an array of words and prints "Found the word!" if it finds the word "python".

words = ["hellos", "python", "pathing"]

def check_for_word(word_to_check, par_words):
    if word_to_check in par_words:
        print("Found the word!")

check_for_word("python", words)