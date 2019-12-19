#!/usr/bin/env python3
import os
import time

# Выбор директорий для копирования
backup_files = input('Введите список файлов и директорий для копирования:')

target_dir = input('\nУкажите путь резервного копирования')
today = time.strftime('%d_%m_%Y')
target_path = target_dir + os.path.sep + today + os.path.sep + time.strftime('%H_%M')+'.tar.gz' # Путь к файлу резервной копии
tar_command = 'tar -czvf {0} {1}'.format(target_path, backup_files)
print(tar_command)
if not os.path.exists(os.path.normpath(target_dir + os.path.sep + today)):
    os.mkdir(target_dir + os.path.sep + today)
print('make path\n', os.path.normpath(target_dir + os.path.sep + today))
if os.system(tar_command) == 0:
    print('Файл tar создан\n {}'.format(target_dir))
else:
    print('Вы создали что-то не так')