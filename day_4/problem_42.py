# Use a for loop to create the following number pattern for a given number of rows

rows = 5 
def create_pattern(par_rows):
    for x in range(par_rows):
        print(f"{x+1}" * (x+1))

create_pattern(rows)
