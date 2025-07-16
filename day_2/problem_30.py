# Print the capital of France.


country = {
        "usa": { "capital": "Washington", "population": 331},
            "france": { "capital": "Paris", "population": 67}
        }
def print_capital(dictionary, key_reference, inner_key_reference):
    return dictionary[key_reference][inner_key_reference]

print(print_capital(country, "france","capital"))

