# Take a sentence and convert all the letters to lowercase, then print it.

sentence = str(input("Enter a sentence: "))

def convert_to_lowercase(sentence):
    return sentence.lower()

print(f"Before convert: {sentence} \nAfter convert: {convert_to_lowercase(sentence)}")