"""Задача 12
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
Пример:
4 4 -> 2 2
5 6 -> 2 3"""

S = int(input('Введите сумму чисел: '))
P = int(input('Введите произведение чисел: '))
D = S**2 - 4*P
print(D)
Y1 = (S + D**0.5) / 2
Y2 = (S - D**0.5) / 2
X1 = S - Y1
X2 = S - Y2
if X1 == Y2 and Y1 == X2:
    print(X1, Y1)
else:
    print(X1, X2, Y1, Y2)