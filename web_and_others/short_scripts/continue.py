name=input('Введите ваше имя:')
while True:
    s = input('Введите любой текст:')
    if s == 'Выход':
        continue
        print('Программа остановлена')
        break
    if len(s)<3:
        print('Слишком мaло символов',name)
        print('Количесво символов:',len(s),name)
        continue
    print('Строка достаточной длины',name)
    print('Количесво символов:',len(s),name)
