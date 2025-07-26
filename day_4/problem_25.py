# Create a nested array and use the each method to print each sub-array and its elements.

numbers = [[1, 2], [3, 4], [5, 6]]

def show_array(par_array):
    for x in range(len(par_array)):
        print(par_array[x])
        
show_array(numbers)