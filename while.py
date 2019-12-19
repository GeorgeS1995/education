number = 23
running = True

while running:
    guess = int(input('Введите целое число:'))

    if  guess == number:
        print('Поздравляем вы выиграли')
        running = False
    elif guess < number:
        print('число больше')
    else:
        print('Число меньше')
else:
    print('Цикл закончен')

print('Завершено')