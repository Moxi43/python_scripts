def is_year_leap():
    k = int(input('Введите год:'))
    if k % 4 == 0:
        print('Этот год является високосным!')
    else:
        print('Этот год не високосный!')

is_year_leap()
