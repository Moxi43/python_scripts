print('Простое присваивание')
shoplist = ['яблоки', 'манго', 'морковь', 'бананы']
mylist = shoplist
del shoplist[0]
print('shoplist:', shoplist)
print('mylist:', mylist)
print('Копирование при помощи полной вырезки')
mylist = shoplist[:]#создаем копию путем полной вырезки
del mylist[0]
print('shoplist:', shoplist)
print('mylist:', mylist)
