# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, 
# a1 = 1, 
# ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# n	…	 −10 −9	−8	−7	−6	−5	−4	−3	−2	−1	0	1	2	3	4	5	6	7	8	9	10	…
# F_{n}	…−55 34	−21	13	−8	 5	−3	 2	−1	 1	0	1	1	2	3	5	8	13	21	34	55	…


def f(n) -> int:
    '''Возвращает чило Фибоначчи по номеру'''
    if n == 0 or n == 1:
        return 1
    return f(n - 1) + f(n - 2)


n = int(input())
print(f(n - 2))


def fib(n):
     if n in [1, 2]:
         return 1
     return fib(n - 1) + fib(n - 2)


n = int(input('введите число: '))
print(fib(n + 1))


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

 
print(fib(int(input())))


def fib(n):
    if n in (1, 2):
        return 1
    return fib(n - 1) + fib(n - 2)

    
print(fib(10))
