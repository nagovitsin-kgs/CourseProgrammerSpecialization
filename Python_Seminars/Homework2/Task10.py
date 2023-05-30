"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
"""
# Идеальное решение после проверки задания:
n = int(input('Введите количество монет: n = '))

count_zero = 0
count_one = 0

for i in range(n):
    x = int(input(f'Ведите любой номинал монет от 0: x{[i]} = ')) # x - это номинал монет, от 0 до ...- любые.
    if x == 0:
        count_zero += 1
    else:
        count_one += 1

if count_one > count_zero: # сравниваем и определяем min кол-во монет, кол-во, которое min - переворачиваем.
    print(f'count_zero = {count_zero} - кол-во этих монет min, значит, переворачиваем {count_zero} - шт.')
else:
    print(f'count_one = {count_one} - кол-во этих монет min, значит, переворачиваем {count_one} - шт.')

# Вариант №1:
from random import randint
import random
n = int(input('Введите количество монет: n = '))

orel = 0
reshka = 0

for i in range(n):
    denomination = int(input(
        'Введите любые монеты номиналом 5 или 10, где Орел(5), Решка(10): '))
    if denomination == 5:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(
        f'Переверните {orel} монет(ы), с Орла на Решку, так как их меньше всего.')
elif orel == reshka:
    print(
        f'Количество Орлов и Решек одинаковое, по {orel} штук, переворачивать не нужно.')
else:
    print(
        (f'Переверните {reshka} монет(ы) с Решки на Орла, так как их меньше всего.'))

# Вариант №2:
n = int(input('Введите количество монет: n = '))

orel = 0
reshka = 0

coins = [10, 5]  # монеты номеналом 10 и 5

for i in range(n):
    random.shuffle(coins)
    print(f'Все монеты: {coins}')
    if int(coins[0]) == 10:
        reshka += 1
    if int(coins[0]) == 5:
        orel += 1
print(f'Всего монет [Орел, Решка]: {orel, reshka}')

if orel > reshka:
    min = reshka
else:
    min = orel

print(
    f"Mинимальное количество монет, которые нужно перевернуть: {min} шт.")
