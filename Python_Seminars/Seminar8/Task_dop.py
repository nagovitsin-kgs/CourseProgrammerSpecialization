# https: // leetcode.com / problems / add - two - numbers /

# Задача: Вам даны два непустых связанных списка, представляющих два неотрицательных целых числа. Цифры хранятся в обратном порядке , и каждый из их узлов содержит одну цифру. Добавьте два числа и верните сумму в виде связанного списка.

# Вы можете предположить, что эти два числа не содержат начальных нулей, кроме самого числа 0.
# Пример 1: (Смотри: https: // leetcode.com / problems / add - two - numbers /)

#  Ввод: l1 = [2, 4, 3], l2 = [5, 6, 4]
#  Вывод: [7, 0, 8]
#  Объяснение: 342 + 465 = 807.

# Пример 2:

#  Вход: l1 = [0], l2 = [0]
#  Выход: [0]

# Пример 3:

#  Ввод: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
#  Вывод: [8, 9, 9, 9, 0, 0, 0, 1]

# Ограничения:

# Количество узлов в каждом связанном списке находится в диапазоне [1, 100].
# 0 <= Node.val <= 9
# Гарантируется, что список представляет собой число, не имеющее лидирующих нулей.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):


#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # создание фиктивной (dummy) ноды для возврата
        dummy = ListNode()
        # установка указателя текущей (curr) ноды на dummy
        curr = dummy
        # инициализация переменной carry для хранения "переноса" в следующий разряд
        carry = 0
        # цикл, который будет выполняться до тех пор, пока l1 или l2 содержат ноды или есть остаток от прошлого разряда (carry)
        while l1 or l2 or carry:
            # инициализация переменной sum как текущей суммы
            sum = carry
            # если l1 не равно None, то добавляем его значение в sum и перемещаемся на следующий узел
            if l1:
                sum += l1.val
                l1 = l1.next
            # если l2 не равно None, то добавляем его значение в sum и перемещаемся на следующий узел
            if l2:
                sum += l2.val
                l2 = l2.next
            # вычисляем carry для следующей итерации
            carry = sum // 10
            # создание новой ноды с результатом текущей суммы в текущем разряде
            curr.next = ListNode(sum % 10)
            # перемещаем указатель на следующую ноду
            curr = curr.next
        # возврат ноды, следующей за фиктивной нодой (dummy)
        return dummy.next


class ListNode:

    def __init__(self, val=0, next=None):
        # инициализация значения текущей ноды (val) и указателя на следующую ноду (next)
        self.val = val
        self.next = next


l1 = [2, 4, 3]
l2 = [5, 6, 4]
