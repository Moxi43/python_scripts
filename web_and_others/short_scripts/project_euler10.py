for a in range(4,500):
    for b in range (4,500):
        if a * a + b * b == (1000 - a - b) ** 2:
            print(a * b * (1000 - a - b))
            print('a равно: ' ,a)
            print('b равно: ' ,b)
            print('с равно: ' + str(1000 - a - b))
