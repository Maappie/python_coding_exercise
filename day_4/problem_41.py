# Ask the user for a sentence, split it into words, and use a for loop to print each word in reverse.

sentence = str(input("Enter a sentence. "))

def show_each_word_in_reverse(sentence):
   words = sentence.split()
   reversed_words = " ".join([word[::-1] for word in words ])
   print(reversed_words)
   
show_each_word_in_reverse(sentence)