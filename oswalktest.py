import os


def file_list(path):
    for a, b, c in os.walk(os.path.normpath(path)):
        print(a, b, c)


backup_files = input('Введите список файлов и директорий для копирования:')
file_list(backup_files)
