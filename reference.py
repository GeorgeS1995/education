print('Простое присваивание')
shoplist = ['Бананы', 'Яблоки', 'Манго', 'Морковь']
mylist = shoplist
del shoplist[0]
print(shoplist)
print(mylist)

print('Копирование при помощи полной вырезки')
mylist = shoplist[:]
del mylist[0]
print(shoplist)
print(mylist)