# Write a program that repeatedly asks the user for input and prints it back to them until they type "exit".

while True:
    string = str(input("Type 'exit' to exit: "))
    
    if string == "exit":
        break
    