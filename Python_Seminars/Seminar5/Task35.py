# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 


# Вариант 1
def is_prime(n: int, divider: int) -> bool:
    """рекурсивная проверка простоты числа"""
    if divider == 1:
        return True
    if n % divider == 0:
        return False
    return is_prime(n, divider - 1)


n = 9
print(is_prime(n, n // 2 + 1))

for i in range(n // 2 + 1, 1, -1):
    print(i, n % i)


# Вариант №2
def isPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n


n = int(input())
if isPrime(n):
    print('YES')
else:
    print('NO')

k = 13

# 1 not being a prime number, is ignored
if k > 1:
    for i in range(2, int(k / 2) + 1):
        if (k % i) == 0:
            print("НЕТ")
            break
    else:
        print("ДА")

else:
    print("It is not a prime number")
