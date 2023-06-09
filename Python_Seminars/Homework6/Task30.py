# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n - го члена прогрессии: an = a1 + (n - 1) * d.
# Каждое число вводится с новой строки.
# Пример:
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# Арифметическая прогрессия является монотонной последовательностью. 
# При d > 0 она является возрастающей, а при d < 0 — убывающей. 
# Если d = 0, то последовательность будет стационарной.

# Пример идеального решения от учителя:
a1 = int(input())
d = int(input())
n = int(input())
for i in range(n):
print(a1 + i * d)

# Вариант №1: (разминка)
a1 = 7
d = 2
n = 5
an = []
for i in range(n):
    an.append(a1 + i * d)
    # print(a1 + i * d, end=' ')
print(*an)

# # Вариант №2:
# Декомпозиция:
# 1. Функции ввода данных: перый элемент (a1), разность (d) и количество элементов (n) с клавиатуры;
# 2. Метод получения n - го члена прогрессии по формуле an = a1 + (n - 1) * d;
# 3. Функция вывода (печать).

a1 = int(input("Введите значение 1-го элемента: \na1 = "))
d = int(input("Введите разность элементов: \nd = "))
n = int(input("Введите количество элементов: \nn = "))


def arithmetic_progression(a1, d, n):
    return [a1 + (i - 1) * d for i in range(1, n + 1)]


an = list()
an = arithmetic_progression(a1, d, n)
print(*an)

# Вариант №3:
n = int(input('n = '))
a = [0] * n
a[0] = int(input('a[0] = '))
d = int(input('d = '))
print(a[0], end=' ')

for i in range(1, n):
    a[i] = a[i - 1] + d
    print(a[i], end=' ')
