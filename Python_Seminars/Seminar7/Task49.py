# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi * a * b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Ввод:

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(list_of_orbits):
#     return list_of_orbits

# print(*find_farthest_orbit(orbits))

# Вывод:
# 2.5 10

# https: // leetcode.com / problems / two - sum / 
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(orbits):
#     pi = 3.14
#     orbits_new = [(0, 0)]
#     max = 0
#     for i in orbits:
#         if i[0] != i[1]:
#             if max < pi * i[0] * i[1]:
#                max = pi * i[0] * i[1]
#                orbits_new.pop()  # если выполняется условие, то удаляем предыдущее значение кортежа
#                orbits_new.append(i)  # и добавляем новое, чтобы в списке оставалась только одно, max
#    return orbits_new[0]  # добавили [0], чтобы распаковывался список

# print(*find_farthest_orbit(orbits))

# 2 вариант решения задачи (убрали из формулы расчета число pi, т.к. это не влияет на нахождение max)

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

# def find_farthest_orbit(list_of_orbits):
#     list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]  # возвращает число из списка, который #                                                                             # он принимает, где 1 элемент не равен 2
#     list_of_areas = [(i[0] * i[1]) for i in list_of_elliptical_orbits]  # возвращает произведение элементов из пред. списка
#     max_area_index = list_of_areas.index(max(list_of_areas))  # находим max из пред.списка
#     return list_of_elliptical_orbits[max_area_index]  # возвращает max элемент

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))


# /////////
def find_farthest_orbit(list_of_orbits):
    list_of_elliptical_orbits = [i for i in list_of_orbits if i[0] != i[1]]
    list_of_areas = [(i[0] * i[1]) for i in list_of_elliptical_orbits]
    max_area_index = list_of_areas.index(max(list_of_areas))
    return list_of_elliptical_orbits[max_area_index]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
# /////////
# import math

# list_of_orbits = [(1, 3), (2.5, 10), (7, 2), (11, 11), (4, 3)]

# def find_farthest_orbit(list_of_orbits):
#     return max(list_of_orbits, key=lambda x: x[0] * x[1] * math.pi if x[0] != x[1] else 0)

# print(find_farthest_orbit(list_of_orbits))
# ////////
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


def find_farthest_orbit(orbits):
    return max(orbits, key=lambda x: x[0] * x[1] if x[0] != x[1] else -1)


print(find_farthest_orbit(orbits))
