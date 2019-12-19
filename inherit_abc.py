from abc import *
import msvcrt


class SchoolMember(metaclass=ABCMeta):
    '''Представляет любого человека в школе'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('Создан SchoolMember: {}'.format(self.name))

    @abstractmethod
    def tell(self):
        '''Вывести информацию'''
        print('Имя: {0} Возраст: {1}'.format(self.name, self.age), end=" ")


class Teacher(SchoolMember):
    '''Представляет преподавателя'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('Создан Teacher: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: {:d}'.format(self.salary))


class Student(SchoolMember):
    '''Представляет студента'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Создан ученик: {}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Оценка: {}'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print('Добавляем:\n 1)Учителя\n 2)Ученика\n 3)Вывод\n 4)Вызвать ошибка TypeError')

members = []
while True:
    key = msvcrt.getch()
    if int(key) == 1:
        a = input('Введите имя учителя: ')
        b = input('Введите возраст учителя: ')
        c = input('Введите зарплату учителя: ')
        temp = Teacher(a, b, c)
        members.append(temp)
        print('Добавляем:\n 1)Учителя\n 2)Ученика\n 3)Вывод\n 4)Вызвать ошибка TypeError')
        print(members)
    elif int(key) == 2:
        a = input('Введите имя ученика: ')
        b = input('Введите возраст ученика: ')
        c = input('Введите оценку ученика: ')
        temp = Studen(a, b, c)
        members.append(temp)
        print('Добавляем:\n 1)Учителя\n 2)Ученика\n 3)Вывод\n 4)Вызвать ошибка TypeError')
        print(members)
    elif int(key) == 3:
        break
    elif int(key) == 4:
        temp = SchoolMember('asd', 'asd')

for member in members:
    member.tell()