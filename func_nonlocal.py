# Filename: func_nonlocal.py
def func_outer():
    x = 2
    print('x равно', x)

    def func_inner():
        global x
        x = 5
    func_inner()
    print('Локальное x сменилось на', x)

func_outer()
print('Локальное x сменилось на', x)