import time


def countdown(i):
    print(i)
    if i > 0:
        time.sleep(0.25)
        i -= 1
        countdown(i)
    else:
        return print('STOP')


countdown(int(input('Залупим?')))