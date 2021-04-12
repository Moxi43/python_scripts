import math
def square():
    k = int(input('Введите сторону квадрата:'))
    p = (k * 4)
    s = (k ** 2)
    d = math.sqrt(k * k * 2)
    j = (p, s, d)
    f = tuple(j)
    print(f)
square()
