
from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.BLACK)
print(Back.WHITE)

what = input('Введите название операции: (+, -, /, *)')

print(Back.WHITE)

a = float(input('Введите первое число:'))

b = float(input('Введите второе число:'))

print(Back.WHITE)

if what == '+':

    c = a + b
    print('Результат:' + str(c))

elif what == '-':

    c = a - b

    print('Результат:' + str(c))

elif what == '/':

    c = a / b

    print('Результат:' + str(c))
elif what == '*':

    c = a * b

    print('Результат:' + str(c))

else:

    print('Выбрана неверная операция')

print('Результат:' + str(c))
