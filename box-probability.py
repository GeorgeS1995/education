def count_v(marbles):
    return "{}/{}".format(marbles.count("w"), len(marbles))


def takewhite(marbleskey):
    list = marbleskey.split("/")
    if int(list[0]) - 1 < 0:
        return marbleskey
    list[0] = int(list[0]) - 1
    return str(list[0]) + "/" + str(list[1])


def takeblack(marbleskey):
    list = marbleskey.split("/")
    if int(list[0]) + 1 > int(list[1]):
        return marbleskey
    list[0] = int(list[0]) + 1
    return str(list[0]) + "/" + str(list[1])


def pwhite(marbleskey):
    list = marbleskey.split("/")
    return int(list[0]) / int(list[1])


def pblack(marbleskey):
    list = marbleskey.split("/")
    return (int(list[1]) - int(list[0])) / int(list[1])


def branch_iter(tree):
    newbranch = dict()
    for i in tree[-1].keys():
        if newbranch.get(takeblack(i)) is None:
            newbranch[takeblack(i)] = pblack(i) * tree[-1][i]
        else:
            newbranch[takeblack(i)] += pblack(i) * tree[-1][i]
        if newbranch.get(takewhite(i)) is None:
            newbranch[takewhite(i)] = pwhite(i) * tree[-1][i]
        else:
            newbranch[takewhite(i)] += pwhite(i) * tree[-1][i]
    tree.append(newbranch)
    return tree


def last_iter_p(tree):
    P = 0
    for i in tree[-1].keys():
        P += tree[-1][i] * pwhite(i)
    return round(P, 2)


def checkio(marbles: str, step: int) -> float:
    tree = []
    startkey = count_v(marbles)
    newbranch = {startkey: 1}
    tree.append(newbranch)
    for i in range(step - 1):
        tree = branch_iter(tree)
    return last_iter_p(tree)


# These "asserts" using only for self-checking and not necessary for auto-testing

if __name__ == '__main__':
    print("Example:")
    print(checkio('bbw', 3))

    assert checkio('bbw', 3) == 0.48, "1st example"
    assert checkio('wwb', 3) == 0.52, "2nd example"
    assert checkio('www', 3) == 0.56, "3rd example"
    assert checkio('bbbb', 1) == 0, "4th example"
    assert checkio('wwbb', 4) == 0.5, "5th example"
    assert checkio('bwbwbwb', 5) == 0.48, "6th example"
    print("Coding complete? Click 'Check' to earn cool rewards!")

