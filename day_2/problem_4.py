# You have an array of colors, Replace "yellow" with "purple" and print the new array.

def change_color(target_color, change_with, list):
    for x in range(len(list)):
        if list[x] == target_color:
            list[x] = change_with
    return list

colors = ["red", "blue", "green", "yellow"]
color = change_color("yellow", "purple", colors)

print(colors)