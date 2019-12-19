def is_palinome(str):
    reversed_string = str[::-1]
    return str == reversed_string

def longest_palindromic(a):
    substring_border = 1
    str_len = len(a)
    while True:
        for i in range(substring_border):
            cur_substring = a[i: str_len - (substring_border - (1 + i))]
            if is_palinome(cur_substring):
                return cur_substring
        substring_border += 1


if __name__ == '__main__':
    print("Example:")
    print(longest_palindromic('abc'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert longest_palindromic('abc') == 'a'
    assert longest_palindromic('abacada') == 'aba'
    assert longest_palindromic('artrartrt') == 'rtrartr'
    assert longest_palindromic('aaaaa') == 'aaaaa'
    print("Coding complete? Click 'Check' to earn cool rewards!")
