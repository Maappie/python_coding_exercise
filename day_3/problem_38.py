# Write a program that loops through two arrays and checks if corresponding elements from each array are equal. 
# Print the index and values if they are equal.

num1 = [1, 2, 3, 4, 5, 3]
num2 = [1, 3, 2, 6, 7, 8]

def check_array(par_num1, par_num2):

    for x in range(len(par_num1)):
        for y in range(len(par_num2)):
            if par_num1[x] == par_num2[y]:
                print(f"The value {par_num1[x]} were equal at index: {x} and {y}")

check_array(num1, num2)