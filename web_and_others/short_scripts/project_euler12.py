def print_factors(x): #Функция для определения количества делителей
    print("The anount of ",x,":")
    for i in range(1, x + 1):
        if x % i == 0:
            rez.append(i) #Делители добавляются в список "rez"
def triangle(n):
    return ((n**2)+2/2.0)

rez = []
k = len(rez)
num = int("600")
'''
print_factors(num)
print(len(rez))'''

n = int(input("Введите n:"))
triangle(n)
