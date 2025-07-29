# Create a variable outside of a function, and use it inside the function

x = "Outside variable"

def function():
    print(x)
    
function()

# local variable inside the function
x = "awesome"

def function():
  x = "fantastic"
  print("Python is " + x)

function()

# global variable inside the function *must call the function first to use global variable

def function():
    global greet 
    greet = "good"
    print("This is from local: " + greet)
function()
print("this is from outside: " + greet)