def nod (a,b):
    while b > 0:
        a,b = b, a % b
    return a

def nok (a,b):
    return a * b // nod(a,b)

d = 1
for i in range(2, 21):
    d = nok(d, i)
print(d)
