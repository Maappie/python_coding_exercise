# Write a program that asks the user to enter some text and checks if the text is empty. If it is, print You entered an empty string.

sentence = str(input("Enter a text: "))

def check_sentence(sentence):
    if sentence.strip() == "":
        print("You entered an empty string.")

check_sentence(sentence)