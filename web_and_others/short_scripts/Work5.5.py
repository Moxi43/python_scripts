phone_book = {}

phone_book['Esther'] = 88005553535
phone_book['Ben'] = 1342304332
phone_book['Bob'] = 334324252224
phone_book['Dan'] = 998493492032

n1 = phone_book['Esther']
n2 = phone_book['Ben']
n3 = phone_book['Bob']
n4 = phone_book['Dan']

q = str(input('Введите имя того, кого хотите найти:'))
if q == 'Esther':
    print(n1)
elif q == 'Ben':
    print (n2)
elif q == 'Bob':
    print(n3)
elif q == 'Dan':
    print(n4)
else:
    print('Этого имени нет в списке!')
