# Create a hash to store information about your favorite movie: title, director, year, and rating. Print the entire hash.

def create_hash(dictionary, key_one, value_one, key_two, value_two, key_three, value_three, key_four, value_four):
    dictionary[key_one] = value_one
    dictionary[key_two] = value_two
    dictionary[key_three] = value_three
    dictionary[key_four] = value_four
    return dictionary

movie = {}
print(create_hash(movie, "title", "Dora the Explorer", "director", "Chris Gifford", "year", 2000, "rating", 8.5))

