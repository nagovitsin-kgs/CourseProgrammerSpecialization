"""
Задача 12:
Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""

# Вариант №1:
x = abs(int(input('Введите первое натуральное число: X = ')))
y = abs(int(input('Введите второе натуральное число: Y = ')))

s = x + y
p = x * y

y1 = int((s + ((-s) ** 2 - 4 * p) ** 0.5) / 2)
x1 = int((s - ((-s) ** 2 - 4 * p) ** 0.5) / 2)

print(x1, y1)

# Вариант №2:
x = abs(int(input('Введите первое натуральное число X от 1 до 1000: ')))
y = abs(int(input('Введите второе натуральное число Y от 1 до 1000: ')))

if x < 1 or x > 1000 or y < 1 or y > 1000:
    print('Вы ввели число не из заданного диапазона!')
else:
    s = x + y
    p = x * y
    stop = 0

    for i in range(1001):
        if stop != 1:
            for j in range(1001):
                if stop != 1:
                    if i * j == p and i + j == s:
                        print(i, j)
                        stop = 1
            else:
                j = 1001
        else:
            i = 1001

# Вариант №3:
s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))

x = (s - int((s ** 2 - 4 * p) ** 0.5)) // 2
y = s - x

if x <= 1000 and y <= 1000:
    print('Петя обманул ')

else:
    print(f'Числа задуманные Петей {x, y} ')
