import msvcrt
import sys


while True:
    key = msvcrt.getch()
    if key == b'q':
        print('Пока')
        sys.exit()
    else:
        print(key)
        print(int(key))

