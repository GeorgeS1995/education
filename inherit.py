import msvcrt


class SchoolMember:
    '''Представляет любого человека в школе'''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Создан член школьного обещства {}'.format(self.name))

    def tell(self):
        '''Вывести информацию'''
        print('\n\nИмя: {0}\nВозраст: {1}'.format(self.name, self.age))

class Teacher(SchoolMember):
    '''Создает учителя'''

    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Создан Учитель: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: {0}'.format(self.salary))

class Studen(SchoolMember):
    '''Создает студента'''

    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Создан Учитель: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: {0}'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Studen('Swaroop', 25, 75)

print('Добавляем:\n 1)Учителя\n 2)Ученика')

members = []
while True:
    key = msvcrt.getch()
    if int(key) == 1:
        a = input('Введите имя учителя: ')
        b = input('Введите возраст учителя: ')
        c = input('Введите зарплату учителя: ')
        temp = Teacher(a, b, c)
        members.append(temp)
        print('Добавляем:\n 1)Учителя\n 2)Ученика\n 3)Вывод')
        print(members)
    elif int(key) == 2:
        a = input('Введите имя ученика: ')
        b = input('Введите возраст ученика: ')
        c = input('Введите оценку ученика: ')
        temp = Studen(a, b, c)
        members.append(temp)
        print('Добавляем:\n 1)Учителя\n 2)Ученика\n 3)Вывод')
        print(members)
    elif int(key) == 3:
        break

for member in members:
    member.tell()