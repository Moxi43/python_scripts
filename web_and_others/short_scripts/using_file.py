poem = '''\
Программирровать весело.
Если работа скучна,
То чтобы придать ей веселый тон -
- используй Python!
'''

f = open('poem.txt', 'w') #Открываем для записи (writing)
f.write(poem)#записываем текст в файл
f.close()#Закрываем файл

f = open('poem.txt')#Если не указан режим по умолчанию, то подразумевается режим чтения (reading)

while True:
    line = f.readline()
    if len(line) == 0: #Нулевая длина обозначает конец файла
        break
    print(line,end='')

f.close()
