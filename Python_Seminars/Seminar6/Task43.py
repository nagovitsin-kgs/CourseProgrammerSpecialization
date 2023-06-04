# Задача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод: Вывод:
# 1 2 3 2 3 2

# 0 (через словарь)
arr = list(map(int, input().split()))
mem = {}

for elem in arr:
    if elem not in mem:
        mem[elem] = 1
    else:
        mem[elem] += 1

count = 0

for elem in mem:
    if mem[elem] > 1:
        count += 1
print(count)

# 1
num_list = [1, 2, 1, 3, 4, 5, 3, 4, 1]
pair_count = sum(num_list.count(i) // 2 for i in set(num_list))

print(pair_count)

# 2
from random import randint

arr = [randint(1, 10) for i in range(
    int(input('Введите количество элементов массива: ')))]

print(arr)

count = 0
for i in range(len(arr) - 1):  # -1 чтобы последний элемент не сравнивался с последним
    for j in range(i + 1, len(arr)):  # +1 чтобы первый элемент не сравнивался с последним
        if arr[i] == arr[j]:
            count += 1
print(count)

# 3
print('Введите список чисел: ')
a = [int(a) for a in input().split()]
b = set()
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            b.add(a[i])
print(len(b))
print(b)
