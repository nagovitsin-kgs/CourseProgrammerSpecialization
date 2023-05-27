"""
Задача 18: 
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

Пример:
5
1 2 3 4 5
6
-> 5"
"""
import random

# Вариант №1:
n = int(
    input("Введите кол-во элементов в массиве: N = "))

a = list(map(int, input(
    f'Ввведите через пробел {n} целых чисел(а) для создания массива А = [1..N]: ').split()))
print(a)

if len(a) != n:
    print("ошибка!")
else:
    x = int(input("Введите искомое число: Х = "))

    k = 0
    min = abs(x - a[0])

    for i in range(len(a[:])):
        count = abs(x - a[i])
        if count < min:
            min = count
            k = i
print(
    f"Самый близкий по величине элемент к заданному числу Х = {x} в массиве A, это элемент c индексом {k}: А[{k}] = {a[k]} ")

# Вариант №2:
n = int(input("Введите кол-во элементов в массиве: N = "))

a = [random.randint(1, n) for i in range(n)]
print(f'A = {a} ')

x = int(input("Введите искомое число: Х = "))

k = 0
min = abs(x - a[0])

for i in range(1, n):
    count = abs(x - a[i])
    if count < min:
        min = count
        k = i

print(
    f"Самый близкий по величине элемент к заданному числу Х = {x} в массиве A, это элемент c индексом {k}: А[{k}] = {a[k]} ")
