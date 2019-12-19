#!/usr/bin/env python3
import os
import time
import zipfile

# Выбор директорий для копирования
backup_files = input('Введите список файлов и директорий для копирования:')

target_dir = input('\nУкажите путь резервного копирования')
today = time.strftime('%d_%m_%Y')

comment = input('Комментарий --> ')
# Путь к файлу резервной копии
if len(comment) == 0:
    zip_name = time.strftime('%H_%M') + '.zip'
else:
    zip_name = time.strftime('%H_%M') + comment.replace(' ', '_') + '.zip'

if not os.path.exists(os.path.normpath(target_dir + os.path.sep + today)):
    os.mkdir(target_dir + os.path.sep + today)
print('make path\n', os.path.normpath(target_dir + os.path.sep + today))

# пакую зипчик, код практически копипаста еще не все понимаю
#z = zipfile.ZipFile(target_path, 'w')
#for root, dirs, files in os.walk(backup_files):
#for file in files:
#    z.write(os.path.join(root, file))
#z.close()
os.chdir(os.path.normpath(target_dir + os.path.sep + today)) #Перехожу в каталог где буду делать зипчик
print('я же правильно выбрал директорию \n')
print(os.getcwd())
z = zipfile.ZipFile(zip_name, 'w')
# Если забыл эту конструкцию, то смотри файл oswalktest.py
for root, dirs, files in os.walk(os.path.normpath(backup_files)):
    for file in files:
        z.write(os.path.join(root, file))
z.close()

if os.path.exists(os.path.normpath(target_dir + os.path.sep + today +os.path.sep + zip_name)):
    print('Файл zip создан\n {}'.format(target_dir))
else:
    print('Вы создали что-то не так')