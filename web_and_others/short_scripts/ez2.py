simple_array = []

for i in range(1, 100):
    digit = int(input("Введите число: "))
    if digit == 0:
        break
    if digit % 8 == 0:
        simple_array.append(digit)

if len(simple_array) == 0:
    print("NO")

else:
    k = round((sum(simple_array) / int(len(simple_array))), 1)
    print("Среднее арифмитическое чисел, кратных 8: " + str(k))
