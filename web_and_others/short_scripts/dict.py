book = dict()

book["apple"] = 13
book["bread"] = 25
book['orange'] = 15
book["milk"] = 42
n = input('Введите название продукта:')
if n == 'яблоко':
    print(book['apple'])
elif n == 'хлеб':
    print(book['bread'])
elif n == 'апельсин':
    print(book['orange'])
elif n == 'молоко':
    print(book['milk'])
else:
    print("Продукта нет в списке")
