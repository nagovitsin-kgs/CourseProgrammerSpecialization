# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и # 
# хочет заменить # все свои минимальные оценки # на максимальные. 
# 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все # максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
# f=int(input(()))
# a=[]
# for _ in range(f): # _ - это не используется переменная.
#     a.append(int(input())


def change_Vasiliy(Vasiliy: list[int]) -> list[int]:
    """Рекурсивная замена макисмальных оценок минимальными"""

    max_Vas = max(Vasiliy)
    min_Vas = min(Vasiliy)
    Vasiliy[Vasiliy.index(max_Vas)] = min_Vas

    if max_Vas not in Vasiliy:
        return Vasiliy
    return change_Vasiliy(Vasiliy)


print(change_Vasiliy([1, 2, 3, 1, 1, 3, 4, 4, 5, 4]))

a = [1, 2, 3, 1, 1, 3, 4, 5, 5, 5]
print(a.index(5))

a[a.index(5)] = 1000
print(a)

n = int(input())
a = list(map(int, input().split()))

min_ = 10
max_ = -10

for el in a:
	if el > max_:
		max_ = el
	if el < min_:
		min_ = el

for i in range(n):
	if a[i] == max_:
		a[i] = min_

print(*a)

a = [int(a) for a in input().split()]
print (a)

max = 0
min = 6
for i in a:
    if i > max: max = i
    if i < min: min = i

for i in range(len (a)):
    if a[i] == max: a[i] = min

print (a)

l = [5, 1, 5, 3, 2, 5, 5, 5]
for i in range(len(l)):
  if l[i] == max(l):
    l[i] = min(l)
print(l)
