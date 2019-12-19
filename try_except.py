try:
    text = input('Введите что-нибудь: ')
except EOFError:
    print('EOF не надо так')
except KeyboardInterrupt:
    print('отмена')
else:
    print('Введено {}'.format(text))