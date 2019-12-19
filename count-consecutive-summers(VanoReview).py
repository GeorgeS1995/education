def count_consecutive_summers(num):
    BL = 1
    iter_count = num // 2 + 3 # прибавляем тройку что б нивилировать округление+что range не захватывает последние число + нужна единичка что б удовлетворить i*2+1 = num
    for i in range(1, iter_count):
        sum = i*2+1
        for j in range(i+2, iter_count):
            if sum == num:
                BL += 1
                break
            elif sum > num:
                break
            sum = j + sum
    return BL


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
