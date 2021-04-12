import math as mth
rez = []
for num in range(2, 2000000):
    if all(num % i != 0 for i in range(2, int(mth.sqrt(num))+ 1)):
        rez.append(num)

print(sum(rez))
