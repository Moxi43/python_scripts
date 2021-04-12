class SchoolMember:
    '''Представляет любого человека в школе'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан SchoolMember: {0})'. format(self.name))
    def tell(self):
        '''Вывести инофрмацию'''
        print('Имя: "{0}"' 'Возраст: "{1}"'. format(self.name, self.age), end = "")

class Teacher(SchoolMember):
    '''Этот класс представляет преподавателя'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Создан Teacher: {0})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Зарплата: "{0:d}"'.format(self.salary))

class Student(SchoolMember):
    '''Этот класс представляет ученика'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Создан Student: {0})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Оценки: "{0}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)

print()#Печатает пустую строку

members = [t, s]
for member in members:
    member.tell()
#Работает как для преподователя, так и для студента
