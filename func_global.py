x = 50

def func():
    global x

    print('x равно {}'.format(x))
    x = 2
    print('заменяем глобальное значение х на {}'.format(x))

func()
print('Значение х вне вызова функции {}'.format(x))
