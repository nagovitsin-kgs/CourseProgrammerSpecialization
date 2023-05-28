# Словари, множества и профилирование.
# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа:
# n - кол-во элементов первого множества.
# m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6 # n и m
# 2 4 6 8 10 12 10 8 6 4 2    # 1 - множество
# 3 6 9 12 15 18              # 2 - множество
# 6 12 # Вывод: Числа без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.


# n1_Set = {2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2}
# m2_Set = {3, 6, 9, 12, 15, 18}
# Декомпозиция:
# 1. Ввод первого числа (n) с клавиатуры (кол-во элементов 1-го множества)
# 2. Ввод второго числа (m) с клавиатуры (кол-во элементов 2-го множества)

n = int(input('n'))
m = int(input('m'))

elements1 = set()
elements2 = set()

for i in range(n):
    elements1.add(int(input('ввес эл')))
print(elements1)

for j in range(m):
    elements2.add(int(input('ввес эл')))
print(elements2)

c = elements1.intersection(elements2)
l = list(c)
l.sort()
print(l)
# n1_Set = set(a)
# m2_Set = set(b)

# n1_Set = set(int(i) for i in elements1.split())
# m2_Set = set(int(i) for i in elements2.split())
# n1_Set = set(int(i) for i in n.split())
# m2_Set = set(int(i) for i in m.split())

# collection_Set = n1_Set.intersection(m2_Set)
# print(collection_Set)

# collection_List = list(collection_Set)
# print(collection_List)

# collection_List.sort()

# print(collection_List)


# l_1 = []
# min = l[0]
# for i in range(len(l)):
#     if l[i] < min:
#         min = l[i]
#         l_1.append(l[i])


# n1 = int(input('Введите количество элементов первого набора чисел: '))
# n2 = int(input('Введите количество элементов второго набора чисел: '))
# arr1 = []
# arr2 = []
# for i in range(n1):
#     arr1.append(int(input('Введите элемент первого массива: ')))
# for j in range(n2):
#     arr2.append(int(input('Введите элемент второго массива: ')))
# arr3 = []
# for i in arr1:
#     if i in arr2 and i not in arr3:
#             arr3.append(i)
# arr3.sort()
# print(arr3)
