# Create two variables, x and y, and swap their values. Print both before and after swapping.

def before_swap(x,y):
    print("x is {:.2f} and y is {:.2f}".format(x,y))
    
def after_swap(x,y):
    x = x + y
    y = x - y
    x = x - y
    print("x is {:.2f} and y is {:.2f}".format(x,y))

x = 10.56
y = 20.32

before_swap(x,y)
after_swap(x,y)