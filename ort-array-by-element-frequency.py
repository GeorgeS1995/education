def frequency_sort(items):
    dict_count_items = {}
    output = []
    for i in items:
        if dict_count_items.get(i) is None:
            dict_count_items[i] = items.count(i)
    sorted_dict = sorted(dict_count_items.items(), key = lambda x : x[1], reverse=True)
    for i in sorted_dict:
        count = 0
        while count < i[1]:
            output.append(i[0])
            count += 1
    return output


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
