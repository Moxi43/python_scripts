shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
name = 'Swaroop'
#Операция индексирования
print('Элемент 0 -', shoplist[0])
print('Элемент 1 -', shoplist[1])
print('Элемент 2 -', shoplist[2])
print('Элемент 3 -', shoplist[3])
print('Элемент -1 -', shoplist[-1])
print('Элемент -2 -', shoplist[-2])
print('Символ 0 -', name[0])

#Вырезка из списка
print('Элементы с 1-го по 3-ий:', shoplist[1:3])
print('Элементы со 2-го до конца', shoplist[2:])
print('Элементы с 1-го по -1:', shoplist[1:-1])
print('Элементы от начала до конца:', shoplist[:])

#Вырезка из строки
print('Символы с 1-го по 3-ий:', name[1:3])
print('Символы с 2-ух до конца:', name[2:])
print('Символы с 1-го до -1-го:', name[1:-1])
print('Символы от начала до конца', name[:])
