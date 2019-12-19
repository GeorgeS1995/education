def maximum (x, y):
    if  x > y:
        return x
    elif x == y:
        return 'equal'
    else:
        return y

s = None
while True:
    if s == 'n':
        break
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print(maximum(a, b))
    s = input('Continue y/n')
print('BB')