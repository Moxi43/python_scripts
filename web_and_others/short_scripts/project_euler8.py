rez = []
for num in range(2000000):
    for i in range(2,num):
        if (num%i==0):
            break
        else:
            rez.append(num)
            break
print(sum(rez))
