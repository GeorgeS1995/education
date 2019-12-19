def PrintMax(a, b):
    if a > b:
        print('{} максимально'.format(a))
    elif a == b:
        print('{0} равно {1}'.format(a, b))
    else:
        print('{} максимально'.format(b))

PrintMax(3, 4)

x = 5
y = 1000

PrintMax(x, y)