# Ask the user to input a sentence, convert the entire sentence to uppercase, and print the result.

sentence = str(input("Enter a sentence: "))

def convert_sentence(sentence):
    return sentence.upper()

print(f"Before convert: {sentence}")

print(f"After convert: {convert_sentence(sentence)}")
    