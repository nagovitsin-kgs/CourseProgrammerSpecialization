# Функции, рекурсия, алгоритмы.
# Что будет на лекции сегодня
# ? Функции
# ? Модули
# ? Рекурсия
# ? Быстрая сортировка
# ? Сортировка слиянием

# Функции:
# Функция — это фрагмент программы, используемый многократно.

# Задача1:
# Необходимо создать функцию sumNumbers(n), которая будет считать сумму всех элементов от 1 до n.

# Решение:

# 1. Необходимо создать функцию: def sumNumbers(n):

# Очень важно понимать одну вещь, сколько аргументов мы передаем, столько и принимаем. 
# Или наоборот сколько аргументов мы принимаем, столько и передаем.
# В нашем случае функция sumNumbers принимает 1 аргумент(n).


# 2. Реализовать решение задачи внутри функции:
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)


sumNumbers(5)
# Так как нам нужны все значения из промежутка [1, n], мы вызываем функцию range, от 1 до n + 1,
# так как range не включает последний элемент. НО возникает вопрос, почему мы здесь используем print()?
# Где же всем известный return, которым мы пользовались на С#? На самом деле, нам не нужно теперь писать void,
# для того чтобы выводить данные, а для того чтобы возвращать значения ставить их тип, все намного проще.
# В Python нет такого понятия как процедура (void). Здесь существует только def. 

# Либо:
n = int(input())  # 5


def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)


sumNumbers(n)  # 15

# Программный код, который мы написали прекрасно справляется с поставленной задачей. 
# Давайте изменим наш код и добавим в него return. НО перед этим давайте вспомним, что делает return:
# 1. Завершает работу функции
# 2. Возвращает значение


def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


print(sumNumbers(5))  # 15

# либо:
n = int(input())  # 5


def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa


print(sumNumbers(n))  # 15


# либо: // создадим переменную
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa  # return - тут фунция завершает свою работу, сколько аргументов передаем, столько и возвращаем.


a = sumNumbers(5)
print(a)  # 15


# ЕСЛИ мы добавим в код после return, что-либо не выдаст код после, так как где return, там работа закончена.
def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa  # return - тут фунция завершает свою работу, сколько аргументов передаем, столько и возвращаем.
    print('stop')  # компилятор выдаст 15, так как return завершил работу. Даже print подсвечиваеться.


print(sumNumbers(5))  # 15


# Если мы передаём аргумент по умолчанию y = "Hello" и выводим sumNumbers(n), то:
def sumNumbers(n, y='Hello'):
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)


sumNumbers(n)  # 15, 'Hello' - выдаст по умолчанию аргумент y


# Если мы передаём второй аргумент y, а принимать будем y = 'qwerty' - sumNumbers(n, 'qwerty'), то:
def sumNumbers(n, y='Hello'):
    print(y)
    summa = 0
    for i in range(1, n + 1):
        summa += i
    print(summa)


sumNumbers(n, 'qwerty')  # 15, 'qwerty' - выдаст аргумент y, который принимаем, а 'Hello' - не выдаст.


# Далее:
def sum_str(*args):  # *args - будем передавать неограниченное кол-во аргументов.
    res = ''  # создадим переменную res с пустой строкой
    for i in args:  # пройдёмся по всем элементам переменной args
        res += i
    return res  # вернём res


print(sum_str('q', 'r', 'f'))  # qrf
print(sum_str('d', 'k', 'g', 'j', 'h'))  # dkgjh
# print(sum_str(1, 2, 3))  # выдаст ошибку TypeError: can only concatenate str (not "int") to str
print(sum_str('1, 2, 3'))  # 1, 2, 3 - положит строку в строку res 
