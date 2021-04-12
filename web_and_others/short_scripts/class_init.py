class Person:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Привет, меня зовут', self.name)
p = Person('Swaroop')
p.sayHi()            
