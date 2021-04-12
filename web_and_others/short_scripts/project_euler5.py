def reverse(text): #Создание фунции, которая переворачивает число
    return text[::-1]

def is_palindrome(text): #Функция, которая проверяет число, полученное от фунции "reverse"
    return text == reverse(text)

def isnt_palindrome(text): #Такая же проверка числа, но только наоборот
    return text != reverse(text)

c = str(998001) #Присваивание значения переменной "с"

c = c.lower() #Приводит число "c" к нижнему регистру
c = "".join(symbol for symbol in c if symbol.isdigit())


if is_palindrome(c): #Если это число палиндром, то оно выводится на экран и программа завершает свою работу
    print(int(c) +' palindrome')
else: #Если это число не палиндром, то этот цикл пытается получить из него палиндром
    c = str(c) #Изменение вида переменной для коректной работы кода
    while isnt_palindrome(c): #Этот цикл вычитает из числа "с" по единице, пока "c" не станет палиндромом
        int(c) - 1

print(c)
