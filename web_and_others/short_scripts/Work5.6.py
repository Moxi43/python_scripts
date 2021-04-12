acc = {}

acc['A'] = 1.5
acc['AA'] = 1.5
acc['AAA'] = 3
acc['AAAA'] = 1.55

n1 = acc['A']
n2 = acc['AA']
n3 = acc['AAA']
n4 = acc['AAAA']

q = str(input('Введите размер батарейки (A, AA, AAA, AAAA): '))

if q == 'A':
    print(str(n1) + ' Вольт')
elif q == 'AA':
    print(str(n2) + ' Вольт')
elif q == 'AAA':
    print(str(n3) + ' Вольт')
elif q == 'AAAA':
    print(str(n4) + ' Вольт')
