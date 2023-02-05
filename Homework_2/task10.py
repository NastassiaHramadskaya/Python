"""Задача 10
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть.
Пример:
5 -> 1 0 1 1 0
2"""

from random import randint
coins_num = int(input('Введите количество монет: '))
head_num, tail_num = 0, 0 # Орёл - head, решка - tail
for _ in range(coins_num):
    temp = randint(0, 1)
    print(temp, end=' ') 
    if temp == 0:
        head_num += 1
    else:
        tail_num += 1
print()
print(head_num, tail_num)
if head_num <= tail_num:
    print(f'Минимальное кол-во переворотов монеток = {head_num}')
else:
    print(f'Минимальное кол-во переворотов монеток = {tail_num}')

