# Write a program that asks the user to enter some text and checks if the string is empty.
# If it is, print You entered an empty string. Otherwise, print You entered: #{input}.

text = str(input("Enter some text: "))

def check_text(par_text):
    if not par_text.strip():
        print("You entered an empty string.")
    else:
        print(f"You entered: {par_text.strip()}")

check_text(text)