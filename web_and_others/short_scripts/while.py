number=23 #Присваивает "number" значение 23
running=True #Запускает блок команд
while running:#Выполняет функцию подзапуска блока команд
    guess = int(input('Введите целое число:'))#
    if guess == number:#
        print('Поздравляю, вы угадали')#
        running=False#Останавливает цикл while
    elif guess<number:
        print('Нет, загаданное число немного больше этого')
    else:
        print('Нет, загаданное число немного меньше этого')
else:
    print('Цикл while закончен')
    print('Завершение')
