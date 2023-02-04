"""
Задача 6
Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех 
цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, 
т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
Пример:
385916 -> yes
123456 -> no
"""

number = int(input('Введите номер билета: '))
num_first = number%1000
num_last = number // 1000
sum_first = 0
sum_last = 0
while num_first > 0:
    i = num_first % 10
    sum_first = sum_first + i
    num_first = num_first // 10
while num_last > 0:
    i = num_last % 10
    sum_last = sum_last + i
    num_last = num_last // 10
if sum_first == sum_last:
    print('yes')
else:
    print('no')