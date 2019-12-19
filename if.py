number = 23
guess = int(input('Ввудите целове число:'))

if guess == number:
    print('''Поздравляю, вы угадали
хотя и не выиграли никакого приза''')
elif guess < number:
    print('Загаданное число больше')
else:
    print('Загаданное число меньше')
print('программа завершена')