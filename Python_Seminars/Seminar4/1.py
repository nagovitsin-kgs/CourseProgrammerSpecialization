# # Ваня:
print('============== версия Вани: ')
n = 1
max_number = 0
while n != 0:
    n = int(input())
    if n != 0 and max_number < n:
        max_number = n
print(f'max_number = {max_number}')
# Петя
print('============== версия Пети: ')
max_number = -1
while n > 0:
    n = int(input())
    if max_number < n:
        max_number = n

print(f'n = {n} ')
print(f'max_number = {max_number}')

# num = int(input())
# max = num
# while num != 0:
#     if num > max and num != 0:
#         max = num
#     num = int(input())
# print(f'{max = }')
