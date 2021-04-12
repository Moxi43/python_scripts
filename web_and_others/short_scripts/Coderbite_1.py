import math
f = 0
k = 0
num = int(input('Enter your number: '))
num = num + 1
for k in range(0, num):
    g = math.factorial(k)
print('Произведение чисел последовательности: ' + str(g))
