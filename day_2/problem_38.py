# rint your birthday by using the elements in the array, Example: (2000-01-01)

numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    ['-', 0]
            ]

year = f"{numbers[0][1]}{numbers[3][1]}{numbers[3][1]}{numbers[1][0]}"
month = f"{numbers[0][0]}{numbers[0][1]}"
day = f"{numbers[0][1]}{numbers[1][1]}"

print(f"{year}-{month}-{day}")