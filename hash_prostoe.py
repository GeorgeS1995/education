letters = { 'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31,
            'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79,
            'w': 83, 'x': 89, 'y': 97, 'z': 101}

def hash(list_l, length):
    i = 0
    total = 0
    while i < len(list_l):
        total += list_l[i]
        i += 1
    return total % length


def format_list(list):
    output_letters = []
    prostoe = []
    for i in list:
        if letters.get(i) != None:
            output_letters.append(i)
            prostoe.append(letters[i])
    return output_letters, prostoe

input_list = list(input('Введите последовательность букв'))

print(input_list)
letters_from_input, prostoe = format_list(input_list)
print(letters_from_input)
print(hash(prostoe, 1000))

