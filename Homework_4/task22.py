'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.'''

from random import randint
N = int(input('Введите количество элементов первого множества: '))
list_1 = []
for i in range(N):
    temp = randint(0, 10)
    list_1.append(temp)
print(list_1) 
M = int(input('Введите количество элементов второго множества'))
list_2 = []
for i in range(M):
    temp1 = randint(0, 10)
    list_2.append(temp1)
print(list_2)
set_1 = set(list_1)
set_2 = set(list_2)
set_3 = set_1.intersection(set_2)
print(set_3)
res = sorted(set_3)
print(res)