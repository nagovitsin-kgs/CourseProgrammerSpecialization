# Задача №37. Решение в группах
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы
# (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3


def reverse(n: int) -> None:
    """Переворот строки рекурсией"""
    if n == 0:
        return print('')
    k = int(input())
    reverse(n - 1)
    return print(k)


n = int(input())
reverse(n)

#  Через составление строки
# def f(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return f(n - 1) + f' {k}'

# n = int(input())
# print(f(n))
