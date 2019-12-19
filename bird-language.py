VOWELS = "aeiouy"

def translate(phrase):
    vowels = set(['a', 'e', 'i', 'o', 'u', 'y'])
    output = []
    i = 0
    while i < len(phrase):
        if phrase[i] in vowels:
            output.append(phrase[i])
            i += 3
        elif phrase[i] != ' ':
            output.append(phrase[i])
            i += 2
        else:
            output.append(phrase[i])
            i += 1
    output = ''.join(output)
    return output

if __name__ == '__main__':
    print("Example:")
    print(translate("hieeelalaooo"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
