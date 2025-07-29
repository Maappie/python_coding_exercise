# create a function by using def and calling it
def this_funtion():
    print("Hello function")
this_funtion()

# passing an iarument to a parameter of a function
def this_is_argument(parameter):
    print(parameter)
this_is_argument("I am argument")

# Arbitrary Arguments, *args is used when you don't know how many arguments are going to be passed to the function
def this_is_args(*names):
    for x in range(len(names)):
        print(names[x])
this_is_args("renz", "sam", "siyan")

# Keyword Arguments, send arguments with key and a value (order is not important as long as key name is specific)
def this_is_key_argument(name_1, name_2, name_3):
    print(name_1)
    print(name_2)
    print(name_3)
this_is_key_argument(name_1="buloy", name_3= "buboy", name_2= "bugoy")

# Arbitrary Keyword Arguments, **kwargs is used when you don't know how many key word arguments are going to be passed to the function (create dictionary)
def  this_is_keyword_args(**names):
    for x in names:
        print(x, names[x])
    
this_is_keyword_args(student_1 = "Mappie", student_2 = "Daneco", student_3 = "Chaves")

# Default Parameter Value, when calling a function and no argument is passed, the default value will be used
def this_is_default_function(name = "Bombardino"):
    print(f"My names is {name}")
this_is_default_function()    
this_is_default_function("Crocodilo")

# Passing a List as an Argument, when you pass a specific datatype to a function, then the parameter will treat it as that
def this_is_datatype_function(data):
    print(data)
places = ["manila", "tondo"]
number = 10
this_is_datatype_function(places)
this_is_datatype_function(number)

# Return values, return a specific value or variable when the function is called
def this_is_return_function(name, age):
    info = f"My name is {name} and I am {age} years old"
    return info
print(this_is_return_function("renz", 21))

# The pass Statement is used wheb you created a function that has no contents
def this_is_pass_function():
    pass
this_is_pass_function()

# Positional-Only Arguments, You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
# positional means that you cannot state the keyword and the value inside when you call a function while keyword only means you cannot pass and argument without stating the keyword and the value inside the function when calling it
# add , / after the parameter to specify that a function can have only positional arguments

def this_is_positional_function(x, /):
    print(x)
this_is_positional_function("good morning")

# add *, before the arguments to specify that a function can have only keyword arguments
def this_is_keyword_only_function(*, greet):
    print(greet)
this_is_keyword_only_function(greet = "happy birthday")

# you can have both keyword and postional 
def this_is_combine_arguments(par_positional, /, *, par_keyword):
    print(par_positional)
    print(par_keyword)
this_is_combine_arguments("I am positional", par_keyword = "I am keyword")

# Recursion, to call the function itself inside a function
def this_is_recursion(x):
    if x > 0:
        print(f"recursion number: {x}")
        this_is_recursion(x-1)
    else:
        return
this_is_recursion(3)


