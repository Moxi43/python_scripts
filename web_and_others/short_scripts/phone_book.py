n = input('Введите имя того, чей номер вы хотите найти:')

phone_book = dict()
phone_book["Oleg"] = 88005553535
phone_book['Zufar'] = 89124567423

if n == 'Oleg':
    print (phone_book["Oleg"])
if n == 'Zufar':
    print (phone_book["Zufar"])
