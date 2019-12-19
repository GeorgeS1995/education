def printmax(x, y):
    '''Выводит максимальное из двух чисел.

Оба значения должны быть целыми числами.'''
    x = int(x)
    y = int(y)

    if x > y:
        print('{} наибольшее'.format(x))
    else:
        print('{} наибольшее'.format(y))

printmax(3,5)
print(printmax.__doc__)

help(printmax)