colors = ["Goldenrod", "Purple", "Salmon", "Turquoise", "Cyan"]

def normalize_case(string):
    return string.casefold()


normalized_colors = map(normalize_case, colors)

for i in normalized_colors:
    print(i)
    