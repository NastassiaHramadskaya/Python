"""Задача 16
Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
Пример:
5
1 2 3 4 5
3
-> 1"""

number_N = int(input('Введите количество элементов в массиве: '))
list_1 = [i for i in range(1, number_N+1)]
print(list_1)
number_X = int(input('Введите число X: '))
res = list_1.count(number_X)
print(res)


