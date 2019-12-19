def safe_pawns(pawns: set) -> int:
    count_of_safe_pawns = set()
    def safe_pawns_pair(pawn1, pawn2):
        def coor_to_number(coor):
            coor_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
            x = coor_dict[coor[0]]
            y = int(coor[1])
            return x, y
        xp1, yp1 = coor_to_number(pawn1)
        xp2, yp2 = coor_to_number(pawn2)
        if yp2 == yp1 - 1 and (xp2 == xp1 + 1 or xp2 == xp1 - 1):
            return True
    for i in pawns:
        pawnscopy = pawns.copy()
        pawnscopy.remove(i)
        for y in pawnscopy:
            if safe_pawns_pair(i, y) is True:
                count_of_safe_pawns.add(i)
    return len(count_of_safe_pawns)

print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")