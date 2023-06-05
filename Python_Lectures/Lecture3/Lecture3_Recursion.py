# Функции, рекурсия, алгоритмы.
# Что будет на лекции сегодня
# ? Функции
# ? Модули
# ? Рекурсия
# ? Быстрая сортировка
# ? Сортировка слиянием

# Рекурсия
# Рекурсия — это функция, вызывающая сама себя.
# С рекурсией Вы знакомы с C  # , в Python она ничем не отличается, давай рассмотрим
# следующую задачу: Пользователь вводит число n. Необходимо вывести n - первых
# членов последовательности Фибоначчи.
# Напоминание: Последовательно Фибоначчи, это такая последовательность, в
# которой каждое последующее число равно сумме 2 - х предыдущих.
# При описании рекурсии важно указать, когда функции надо остановиться и
# перестать вызывать саму себя. По - другому говоря, необходимо указать базис
# рекурсии

# Рекурсия
# Решение:


def fib(n):
    # if n in [1, 2]:
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(9))  # для примера

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)  # [1, 1, 2, 3, 5, 8, 13, 21, 34]
