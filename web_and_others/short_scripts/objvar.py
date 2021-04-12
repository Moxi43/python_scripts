class Robot:
    '''Предствляет робота с именем'''
    #Переменная класса, содержащая количество объектов
    population = 0
    def __init__(self,name):
        '''Инициализация данных'''
        self.name = name
        print('(Инициализация {0})', format(self.name))
        #При создании этой личности, робот добовляется к переменной population
        Robot.population += 1
    def __del__(self):
        '''Я умираю'''
        print('{0} уничтожается'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
           print('{0} был последним'.format(self.name))
        else:
            print('Осталось {0:d} работающих роботов'. format(Robot.population))
    def sayHi(self):
        '''Приветствие робота.
        Да, они это могут'''
        print('Приветствую, мои хозяева называют меня {0}'. format(self.name))
    def howMoney():
        '''Выводит численность роботов'''
        print('У нас {0:d} роботов'. format(Robot.population))
    howMoney = staticmethod(howMoney)
droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMoney()
droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMoney()
print('\nЗдесь роботы могут проделать какую-нибудь работу\n')
print('Роботы закончили свою работу, давайте уничтожим их')
del droid1
del droid2

Robot.howMoney()
