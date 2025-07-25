# Create a program that asks the user for two numbers: how many times to iterate and a word to print.
# Use the loop to print the word that many times, with each word on a new line.

number = int(input("How many times to iterate? "))
word = str(input("Word to iterate? "))

def loop():
    for _ in range(number):
        print(word)
        
loop()
