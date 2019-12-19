from typing import List

def checkio(game_result):
    lines = game_result
    game_result = ''.join(game_result)
    print(game_result)
    lines += [game_result[i::3] for i in range(3)]
    print(lines)
    lines += [game_result[0::4], game_result[2:8:2]]
    print(lines)
    for ch in 'OX':
        if ch * 3 in lines:
            print(lines)
            print(ch*3)
            return ch
    return 'D'

if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")