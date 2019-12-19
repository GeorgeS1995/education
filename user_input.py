def reverse(text):
    znaki = ['.', ' ', ',',]
    for i in znaki:
        text.replace(i, '')
    return text

def is_palindrome(text):
    if text == reverse(text):
        print('Палиндроме')
    else:
        print('Не палиндроме')

Something = input('Введите слово: ')
is_palindrome(Something)
