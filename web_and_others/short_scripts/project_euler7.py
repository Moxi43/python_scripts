rez = []
number = 0
for number in range(1, 101):
     rez.append(number)
b = sum(number*number for number in rez)
c = sum(rez)
c = c * c

print(b - c)
