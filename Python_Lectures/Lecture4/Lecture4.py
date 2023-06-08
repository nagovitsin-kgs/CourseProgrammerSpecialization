# Знакомство с языком Python (лекции)
# Урок 4. Функции высшего порядка, работа с файлами

# Что будет на лекции сегодня
# ● Анонимные, lambda -функции
# ● Функция map
# ● Функция filter
# ● Функция zip
# ● Функция enumerate
# ● Файлы
# ● Модуль os
# ● Модуль shutil

# ● Анонимные, lambda -функции:


# На предыдущей лекции мы с Вами обговорили создание и
# использование функций в Python, но некоторые функции могут
# понадобиться всего раз за всю работу приложения. Как можно
# обойтись без их явного описания? Как сократить подобный код?
def f(x):
    return x ** 2


print(f(2))  # 4
# Функция в примере занимает всего две строчки кода, но в
# дальнейшем размеры описания функций будут увеличиваться. И
# тогда сокращение кода будет актуальным.

# Анонимные, lambda -функции


# Какой тип данных у функции? → < class “function” >
# У функции есть тип, значит мы можем создать переменную типа функции и положить в эту
# переменную какую - то другую функцию.
def f(x):
    return x ** 2


g = f
print(f(4))  # 16
print(g(4))  # 16 
# Теперь в контексте этого приложения g может использоваться точно так же, как и f.
# g — это переменная, которая хранит в себе ссылку на функцию.

# Зачем это может потребоваться?


# Анонимные, lambda -функции
# Есть некая функция calc, которая принимает в качестве аргумента число, а в качестве результата
# возвращает это число + 10:
def calc1(x):
    return x + 10


print(calc1(10))  # 20
# Если мы добавим в код не только сложение, но и умножение, деление и вычитание, внутри
# одного кода будем плодить одинаковую логику.

# Достаточно взять функцию calc, которая будет в качестве аргумента принимать операцию и чтото выдавать.


def calc2(x):
    return x * 10


def math(op, x):
    print(op(x))


math(calc2, 10)  # 100


# Анонимные, lambda -функции
# Попробуем описать ту же логику для функции с двумя переменными.
# op — операция, воспринимаем её как отдельную функцию. В примере это либо сумма (sum), либо
# перемножение(mylt):
def sum(x, y):
    return x + y


def mylt(x, y):
    return x * y


def calc(op, a, b):
    print(op(a, b))


calc(mylt, 4, 5)  # 20


# Анонимные, lambda -функции
# Можно создать псевдоним для функции сложения (f).
def sum(x, y):
    return x + y


def calc(op, a, b):
    print(op(a, b))


f = sum
calc(f, 4, 5)  # 9


# В Python есть механизм, который позволяет превратить подобный вызов во что-то более
# красивое — это lambda.
def sum(x, y):
    return x + y


# ⇔ (равносильно)
sum = lambda x, y: x + y  # это тоже самое, что выше def sum.


# Анонимные, lambda -функции
# Теперь, чтобы вызвать функцию суммы, достаточно просто вызвать sum.
# Также можно пропустить шаг создания переменной sum и сразу вызвать lambda:
def calc(op, a, b):
    print(op(a, b))


calc(lambda x, y: x + y, 4, 5)  # 9

# Итак:
# 1. Сначала мы избавились от классического описания функций.
# 2. Затем научились описывать лямбды, присваивая результат какой - то переменной.
# 3. После избавились от этой переменной, пробрасывая всю лямбду в качестве функции.

# Задача для самостоятельного решения
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]

# Решение:
data = [1, 2, 3, 5, 8, 15, 23, 38]
out = []
for i in data:
    if i % 2 == 0:
        out.append((i, i ** 2))

print(out)


# Как можно сделать этот код лучше, используя lambda? # select - выбирать # where - где
def select(f, col):
    return [f(x) for x in col]


def where(f, col):
    return [x for x in col if f(x)]


data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
res = where(lambda x: x % 2 == 0, res)
print(res)  # [2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))
print(res)  # [(2, 4), (8, 64), (38, 1444)]

# ● Функция map:

# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с новыми объектами.
# Есть набор данных. Функция map позволяет увеличить каждый объект на 10.
# f(x) => x + 10
# map(f, [1, 2, 3, 4, 5]) выведет все значения +10 # [11, 12, 13, 14, 15]

# Функция map
list_1 = [x for x in range (1, 20)]
list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)  # [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?
# 1. Маленькое отступление, функция строка.split() - убирает все пробелы и создаем список из
# значений строки, пример:
data = '1 2 3 5 8 15 23 38'.split()
print(data)  # ['1', '2', '3', '5', '8', '15', '23', '38']

# 2. Теперь вернемся к задаче. С помощью функции map():
data = list(map(int, input().split()))  # int/str - вывод итерировано, (input().split()) - это ввод/действие/ф-цию - принимает.
print(data)  # ввод: 1 2 3 вывод [1, 2, 3]


# Функция map
# Результат работы map() — это итератор. По итератору можно пробежаться только один раз. Чтобы
# работать несколько раз с одними данными, нужно сохранить данные (например, в виде списка).
# Как можно сделать этот код лучше, используя map()?
# map() позволит избавиться от функции select.
def where(f, col):
    return [x for x in col if f(x)]


data = '1 2 3 5 8 15 23 38'.split()
res = map(int, data)
res = where(lambda x: x % 2 == 0, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)  # [(2, 4), (8, 64), (38, 1444)]