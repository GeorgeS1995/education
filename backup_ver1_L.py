#!/usr/bin/env python3
import os
import time

# Выбор директорий для копирования
backup_files = input('Введите список файлов и директорий для копирования:')

target_dir = input('\nУкажите путь резервного копирования')
target_path = target_dir + os.path.sep + time.strftime('%d%m%Y%H%M')+'.tar.gz'
tar_command = 'tar -czvf {0} {1}'.format(target_path, backup_files)
print(tar_command)

if os.system(tar_command) == 0:
    print('Файл tar создан\n {}'.format(target_dir))
else:
    print('Вы создали что-то не так')