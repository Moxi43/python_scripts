import pickle

class people:
    def __init__(self, name, lastname):
        self.name = name
        self.lastname = lastname
    def tell(self):
        '''Вывод информации'''
        print('Имя: "{0}"' 'Фамилия: "{1}"'.format (self.name, self.lastname),end="")

ab = { name : lastname
     }
    if name in ab:
         print('Фамилия', ab[name])

namelistfile = 'name.data'
f = open(namelistfile, 'wb')
pickle.dump(ab, f)
f.close()

def del():
    del ab[name,lastname]

name = input('Введите имя:')
lastname = input('Введите фамилию:')
people.tell()
