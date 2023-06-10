# Учитывая массив целых чисел nums и целое число target, верните индексы двух чисел так, чтобы они составляли в суммеtarget .

# Вы можете предположить, что каждый вход будет иметь ровно одно решение , и вы не можете использовать один и тот же элемент дважды.

# Вы можете вернуть ответ в любом порядке.

# Пример 1:

# Ввод: nums = [2, 7, 11, 15], target = 9
#  Вывод: [0, 1]
#  Объяснение: Поскольку nums[0] + nums[1] == 9, мы возвращаем [0, 1].
# Пример 2:

# Ввод: числа = [3, 2, 4], цель = 6
#  Вывод: [1, 2]
# Пример 3:

# Ввод: числа = [3, 3], цель = 6
#  Вывод: [0, 1]

# Ограничения:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109

# nums = [int(x) for x in input().split()]
# target = int(input())

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):
#         if nums[i] + nums[j] == target:
#             print(i, j)

# def two_sum(seq, target):
#     mem = {}
#     for i in range(len(seq)):
#         if target - seq[i] in mem:
#             print(i, mem[target - seq[i]])
#         else:
#             mem[seq[i]] = i


def two_sum(seq, target):
    mem = {}
    for i in range(len(seq)):
        if target - seq[i] in mem:
            return (i, mem[target - seq[i]])
        else:
            mem[seq[i]] = i
    return None
