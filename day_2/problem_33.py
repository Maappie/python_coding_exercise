# Print the name of player2 in Team B

players = {
    "team_a": {"player_1": "John", "player_2": "Paul"}, 
    "team_b": {"player_1": "Sarah", "player_2": "Lucy"}
            }
def show_name(dictionary, key_reference, inner_key_reference):
    return dictionary[key_reference][inner_key_reference]

print(show_name(players, "team_b", "player_2"))


 