
d = int(input('Введите день: '))
m = int(input('Введите месяц: '))
y = int(input('Введите год: '))
print('Выбран этот год: ' + str(d)+'.'+str(m)+'.'+str(y))
def date():

    if d in range(32) and m in range(8, 10, 12) and y in range(3000):
        print ('Такой год существует!')
    elif d in range(32) and m in range(8, 10, 12) and y in range(3000):
        print ('Такой год существует!')
    elif d in range(32) and m == 1 and y in range(3000):
        print ('Такой год существует!')
    elif d in range(29) and m == 2 and y in range(3000):
        print ('Такой год существует!')
    elif d == 29 and m == 2 and y % 4 == 0:
        print ('Високосный год!')
    elif d in range(31) and m in range(2, 4, 6) and y in range(3000):
        print ('Такой год существует!')
    elif d in range(31) and m in range(9, 11) and y in range(3000):
        print ('Такой год существует!')
    else:
        print ('Такого года не существует!')
    
date()
