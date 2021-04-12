numbers_array = []
numbers_array2 = []

for i in range(1, 1000):

    digits = int(input("Введите число: "))
    numbers_array2.append(digits)
    if digits == 0:
        break

    if digits % 3 == 0 and digits % 2 != 0:
        numbers_array.append(digits)

numbers_array.append(digits)

print("Количество чисел: "+str(len(numbers_array2)-1)+"  "+"Количество нечётных чисел, кратных 3: "+str(len(numbers_array)))