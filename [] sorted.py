
a = list(input('Последовательность скобок'))
temp = 0
for i in a:
    if temp < 0:
        print('Закрывающая скобка до открывающей')
        exit()
    elif i == '[':
        temp += 1
    elif i == ']':
        temp -= 1

if temp == 0:
    print('скобки корректны')
else:
    print('Не хватает закрывающей скобки')
