x = 50
def func(x):
    print('x равен {}'.format(x))
    x = 2
    print('Локальное значение переменно {}'.format(x))

func(x)

print('Отображение x не из функции'.format(x))
