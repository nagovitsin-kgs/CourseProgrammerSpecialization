"""
Задача №9. По данному целому неотрицательному n вычислите
значение n!. 
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 
0! = 1 
Решить задачу используя цикл while
Input: 5
Output: 120
Факториал — функция, определённая на множестве неотрицательных целых чисел.
Название происходит от лат. factorialis — действующий, производящий, умножающий;
бозначается n!, произносится эн факториа́л.
Факториал натурального числа n определяется как произведение всех натуральных чисел
от 1 до n включительно:
n! = 1 * 2 * 3 * ... * n
5! = 1 * 2 * 3 * 4 * 5 = 120
Для n = 0 принимается в качестве соглашения, что 0!= 1
"""

# 5! = 1 * 2 * 3 * 4 * 5 = 120

# Вариант решения №1:

i = 1
n = int(input("Введите целое не отрицательное число: "))
res = 1

if n == 0:
    print(f"{n}! = {1} ")
else:
    while i <= n:
        res *= i
        i += 1
    print(f"{n}! = {res} ")

# # Вариант решения №2: (лучший вариант)

count = 1
factorial = 1
n = int(input("Введите целое не отрицательное число: "))

while n >= count:
    factorial *= count
    count += 1
print(f"{n}! = {factorial} ")

# Вариант решения №3 (через функцию)


def factorial(n):
    count = 1
    result = 1
    while count <= n:
        result *= count
        count += 1
    return result


n = int(input("Введите целое не отрицательное число: "))
rw = factorial(n)
print(f"{n}! = {rw} ")