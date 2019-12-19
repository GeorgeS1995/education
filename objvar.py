class Robot:
    '''Представляет робота с именем.'''
    # Переменная класса содержащая количество роботов
    population = 0

    def __init__(self, name):
        '''Инициализация данных'''
        self.name = name
        print('Инициализация {0}'.format(self.name))
        Robot.population += 1
    def __del__(self):
        '''Я умираю.'''
        print('{} уничтожается!'.format(self.name))
        Robot.population -= 1

        if Robot.population == 0:
            print('{0} был последним'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов'.format(Robot.population))

    def sayhi(self):
        '''Приветствие робота.

        Да они это могут.'''
        print('Я робот по имени {}'.format(self.name))

    def howMany():
        '''Выводит численность роботов.'''
        print('У нас {0:d} роботов'.format(Robot.population))

    howMany = staticmethod(howMany)

droid1 = Robot('R2-D2')
droid1.sayhi()
Robot.howMany()

droid2 = Robot('C-3P0')
droid2.sayhi()
Robot.howMany()

print("\nРоботы сделали что-то\n")

print("Роботы больше не нужны.")

del droid1
del droid2

Robot.howMany()