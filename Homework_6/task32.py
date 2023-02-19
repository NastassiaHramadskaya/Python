'''Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''

from random import randint
N = int(input('Введите количество элементов массива: '))
list_1 = []
for i in range(N):
    temp = randint(0, 10)
    list_1.append(temp)
min_number = int(input("Введите минимальный элемент: "))
max_number = int(input("Введите максимальный элемент: "))
for i in range(len(list_1)):
    if min_number < list_1[i] < max_number:
        print(i)