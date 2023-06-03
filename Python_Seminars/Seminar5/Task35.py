# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 


def is_prime(n: int, divider: int) -> bool:
    """рекурсивная проверка простоты числа"""
    if divider == 1:
        return True
    if n % divider == 0:
        return False
    return is_prime(n, divider - 1)


n = 11
print(is_prime(n, n // 2 + 1))

for i in range(n // 2 + 1, 1, -1):
    print(i, n % i)
