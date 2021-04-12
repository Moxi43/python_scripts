a, b, x ,t = 1, 2, 1, 0
while a < 4000000:
    x = b - x
    a = a + x
    b = a
    if x % 2 == 0:
        t += x
    print(str(t) + 'Сумма четных')
