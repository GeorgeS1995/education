class Person:
    def __init__(self, name):
        self.name = name
    def sayhi(self):
        global q
        print("hi, i'm a class {0} ".format(self.name))


P = Person('Person')
P.sayhi()

