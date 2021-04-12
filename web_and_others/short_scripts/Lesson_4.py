def bank():
    a = int(input('Введите сумму вашего вклада:'))
    k = a * 0.1
    years = int(input('На сколько лет вы хотите создать вклад:'))
    f = (0.1 * years) * k
    n = 0
    if years < 1:
        print ('Итоговая сумма вашего вклада:' + a)
    elif years > 1:
        n = float(a) + (float(k) * float(years)) + (float(f) * float(years))
    else:
        n = float(a) + (float(k) * float(years))
    print('Итоговая сумма вашего вклада:' + str(n))
bank()
