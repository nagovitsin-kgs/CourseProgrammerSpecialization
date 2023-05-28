# Словари,множества и профилирование
# 25. Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам
# с помощью постфикса формата _n.

# sequence = 'a a a b a c b b d'.split()
# letters = {}
# result = ''
# for i in range(len(sequence)):
#     if sequence[i] not in letters.keys():
#         letters[sequence[i]] = 1
#         result += f'{sequence[i]} '
#     else:
#         result += f'{sequence[i]}_{letters[sequence[i]]} '
#         letters[sequence[i]] += 1
# print(result)

# решение через срезы

# result = ''
# for i in range(len(sequence)):
#     if sequence[0:i:].count(sequence[i]) == 0:
#         result += sequence[i]
#     else:
#         result += f'{sequence[i]}_{sequence[0:i].count(sequence[i])}'
#     print(sequence[0:i], result)
# print(result)

# # решение через list comprehenshion и срезы

# print(sequence)
# result = [(sequence[i] if
#            sequence[0:i:].count(sequence[i]) == 0 else
#            f'{sequence[i]}_{sequence[0:i:].count(sequence[i])}')
#           for i in range(len(sequence))]
# print(' '.join(result1))

# s = input().split()
# s = 'a a a b a c b b d'.split()
# l = {}
# r = ''
# for i in range(len(s)):
#     if s[i] not in l.keys():
#         l[s[i]] = 1
#         r += f'{s[i]} '
#     else:
#         r += f'{s[i]}_{l[s[i]]} '
#         l[s[i]] += 1
# print(r)

s = 'a a a b a c b b d'.split()
r = ''
for i in range(len(s)):
    if s[0:i:].count(s[i]) == 0:
        r += s[i]
    else:
        r += f'{s[i]}_{s[0:i].count(s[i])}'
    print(s[0:i], r)
print(r)
