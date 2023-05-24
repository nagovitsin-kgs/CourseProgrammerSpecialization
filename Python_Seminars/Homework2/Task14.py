"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""

# Вариант №1:
n = int(input('Введите целое число больше 1: n = '))

k = 1

while k <= n:
    print(k, end=' ')
    k = k * 2

# Вариант №2:

n = abs(int(input('\nВведите число: n = ')))

stop = 0
p = 2

for i in range(n):
    if stop != 1:
        p = p ** i
        if p <= n:
            print(p, end=' ')
            p = 2
        else:
            stop = 1
    else:
        i = n
