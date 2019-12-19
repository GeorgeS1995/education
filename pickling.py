import pickle


# Имя файлаб в котором будет храниться объект
shoplistfile = 'shoplist.data'
# Список покупок
shoplist = ['apple', 'mango', 'carrot']

#Запись в файл
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f) # помещает объект в файл
f.close()

del  shoplist

#Считываем из дампа
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f) # загрузка из файла
print(storedlist)