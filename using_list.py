shoplist = ['apple', 'banana', 'milk', 'carrot']
print('i have to buy {}'.format(len(shoplist)))

print('shops:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\ni forgot a sosagies')
shoplist.append('sosagies')
print('my shoplist now is: {}'.format(shoplist))

print('sort of the shoplist')
shoplist.sort()
print('my shoplist after sort is {}'.format(shoplist))

print('first shop is {}'.format(shoplist[0]))
olditem = shoplist[0]
del shoplist[0]
print('i bought a {}'.format(olditem))
print('my shoplist now is {}'.format(shoplist))