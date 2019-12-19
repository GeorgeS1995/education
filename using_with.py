import time

with open('poem.txt') as f:
    for i in f.read():
        print(i, end='', flush=True)
        time.sleep(0.1)