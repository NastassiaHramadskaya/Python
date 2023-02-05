"""
Задача 14
Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
Пример:
10 -> 1 2 4 8"""

number = int(input('Введите число: '))
temp, power = 1, 1
while temp < number:
    print(temp, end=" ")
    temp = 2 ** power
    power += 1
    
