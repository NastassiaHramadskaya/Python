'''Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, 
разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: 
an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''

a = int(input('Введите первый элемент арифметической прогрессии: '))
b = int(input('Введите разность элементов арифметической прогрессии: '))
c = int(input('Введите количество элементов арифметической прогрессии: '))

for i in range(c):
    print(a + i*b)