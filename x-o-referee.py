from typing import List

def checkio(game_result: List[str]) -> str:
    for y in range(3):
        if game_result[y][0] == game_result[y][1] == game_result[y][2] and game_result[y][0] != '.':
            return game_result[y][0]
    for x in range(3):
        if game_result[0][x] == game_result[1][x] == game_result[2][x] and game_result[0][x] != '.':
            return game_result[0][x]
    if (game_result[0][0] == game_result[1][1] == game_result[2][2] or game_result[0][2] == game_result[1][1] == game_result[2][0]) and game_result[1][1] != '.':
        return game_result[1][1]
    else:
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