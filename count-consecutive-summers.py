def count_consecutive_summers(num):
    BL = 0
    for i in range(1, num + 1):
        start_v = i
        if start_v == num:
            BL += 1
            break
        priv_num = i
        next_num = priv_num + 1
        while True:
            next_num = priv_num + next_num
            if next_num == num:
                BL += 1
                break
            elif next_num > num:
                break
            if priv_num == i:
                priv_num += 1
            priv_num += 1
    return BL


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
