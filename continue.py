while True:
    s = input('Введите что-нибудь:')
    if s == 'exit':
        break
    if len(s) < 3:
        print('слишком короткая строка')
        continue
    print('Введенная строка достаточной длины')
