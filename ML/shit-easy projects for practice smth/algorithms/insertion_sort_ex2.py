#Добавление двух nбитных значений, собранных в два nэлементых массива. Сумма двух цифр должна быть собрана в двочиной системе
# в массиве C

A = [bin(10), bin(1), bin(4), bin(3)]
B = [bin(11), bin(2), bin(5), bin(5)]
C = [bin(0), bin(0), bin(0), bin(0), bin(0)]
n = len(A)
for i in range(n + 1):
    C[i] = 0
carry = 0
for i in range(n, 1):
    C[i] = (A[i] + B[i] + carry) % 2
    carry = (A[i] + B[i] + carry) / 2
    C[i] = carry
print(C)
