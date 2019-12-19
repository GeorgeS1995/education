

def evklid_alg(A, B):
    if max(A,B) % min(A,B) == 0:
        return print(min(A,B))
    else:
        evklid_alg(min(A,B), max(A,B) % min(A,B))

A = int(input('Сторона А:'))
B = int(input('Сторона B:'))

evklid_alg(A, B)
