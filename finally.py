import time


try:
    f = open('poem.txt')
    for i in f.read():
        print(i, end='', flush=True)
        time.sleep(0.1)
except KeyboardInterrupt:
    print('!! Вы отменили чтение файла')
finally:
    f.close()
    print('\n(Очистка: Закрытие файла)')