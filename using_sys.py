import sys
import os

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\n\nПеременная PYTHOPATH содержит', sys.path,'\n')