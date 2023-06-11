# Задача №49. Решение в группах (https://docs-python.ru/tutorial/metody-fajlovogo-obekta-potoka-python/metod-file-read/) - это документация.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные.
# 2. Программа должна сохранять данные в текстовом файле.
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека).
# 4. Использование функций.
# Ваша программа не должна быть линейной.
'''
# Файлы:

# Файлы в текстовом формате используются для:
# ● Хранения данных
# ● Передачи данных в клиент - серверных проектах
# ● Хранения конфигов
# ● Логирования действий

# Что нужно для работы с файлами:
# 1. Завести переменную, которая будет связана с этим текстовым файлом.
# 2. Указать путь к файлу.
# 3. Указать, в каком режиме мы будем работать с файлом.

# Файлы:

# Варианты режима (мод): a, r, w

# a – открытие для добавления данных.
# ○ Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, то файл будет создан и в него начнется запись.

# r (readlines()) – открытие для чтения данных.
# ○ Позволяет читать данные из файла.
# ○ Если вы попробуете считать данные из файла, которого не существует, программа выдаст ошибку.

# w (writelines) – открытие для записи данных.
# ○ Позволяет записывать данные и создавать файл, если его не существует.

# writelines() - Для записи строк из списка в файл используется метод writelines (). Этот метод записывает строки в файл по очереди, без разделителя. Пример его использования: lines= [" Это первая строка\n", " А вот и вторая\n", " И третья — последняя\n"] with open (" output_2.txt", " w", encoding=" UTF-8") as file_out: file_out.writelines (lines). Содержимое выходного файла: Это первая строка А вот и вторая И третья — последняя.

# Файлы:

# Миксованные режимы:

# 1. w +
# ○ Позволяет открывать файл для записи и читать из него.
# ○ Если файла не существует, он будет создан.

# 2. r +
# ○ Позволяет открывать файл для чтения и дописывать в него.
# ○ Если файла не существует, программа выдаст ошибку.

# Файлы:

# Примеры использования различных режимов в коде:

# 1. Режим a (a – открытие для добавления данных)
"""
colors = ['red', 'green', 'blue']
data = open('file.txt', 'a')  # здесь указываем режим, в котором будем работать
data.writelines(colors)  # разделителей не будет
data.close()
"""
# ● data.close() — используется для закрытия файла, чтобы разорвать подключение файловой
# переменной с файлом на диске.
# ● exit() — позволяет не выполнять код, прописанный после этой команды в скрипте.
# ● В итоге создаётся текстовый файл с текстом внутри: redbluedreen.
# ● При повторном выполнении скрипта redbluedreenredbluedreen — добавление в
# существующий файл, а не перезапись файлов.

# Ещё один способ записи данных в файл: (write - писать), (with - с, в, на, с помощью)
"""
with open('file.txt', 'w') as data:
    data.write('line 1\n')
    data.write('line 2\n')
"""
# 2. Режим r (r – открытие для чтения данных)

# ● Чтение данных из файла:(path -путь), (line - строка)
"""
path = 'file.txt'
data = open(path, 'r')
for line in data:
    print(line)  # выведет что в файле file.txt на экран
data.close()
"""
# Файлы
# 3. Режим w (w – открытие для записи данных)
"""
colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
data.writelines(colors)  # разделителей не будет
data.close()
"""
# ● В итоге создаётся текстовый файл с текстом внутри: ‘redbluedreen’.
# ● В случае перезаписи новые данные записываются, а старые удаляются.
'''
# choose_action (выбрать действие)
# phonebook (телефонная книга)
# user_choice (выбор полльзователя)
# file_to_add (можно добавить файл)
# contact_list (список контактов)
# import_data (импортировать данные)
# read_file_to_dict (прочитать файл для диктовки)
# find_number (найти число, номер)
# add_phone_number (добавить номер телефона)
# change_phone_number (изменить номер телефона)
# delete_contact (удалить контакт)
# show_phonebook (показать телефонную книгу)
# continue (продолжать)
# try (пытаться, попытка)
# with (с, с помощью)
# readlines (чтение строки)
# except (кроме, за исключением)
# encoding (кодирование)
# utf-8 (формат преобразования Юникода, 8-бит») — распространённый стандарт кодирования символов)
# new_contacts (новые контакты)
# contacts_to_add (контакты для добавления)
# writelines (записать строки, создать файл, если его не существует)
# File Not Found Error (Ошибка "Файл не найден")


def choose_action(phonebook):
    while True:
        print('Что вы хотите сделать?')
        user_choice = input('1 - Импортировать данные\n2 - Найти контакт\n3 - Добавить контакт\n\
4 - Изменить контакт\n5 - Удалить контакт\n6 - Просмотреть все контакты\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            file_to_add = input('Введите название импортируемого файла: ')
            import_data(file_to_add, phonebook)
        elif user_choice == '2':
            contact_list = read_file_to_dict(phonebook)
            find_number(contact_list)
        elif user_choice == '3':
            add_phone_number(phonebook)
        elif user_choice == '4':
            change_phone_number(phonebook)
        elif user_choice == '5':
            delete_contact(phonebook)
        elif user_choice == '6':
            show_phonebook(phonebook)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue


def import_data(file_to_add, phonebook):
    try:
        with open(file_to_add, 'r', encoding='utf-8') as new_contacts, open(phonebook, 'a', encoding='utf-8') as file:
            contacts_to_add = new_contacts.readlines()
            file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f'{file_to_add} не найден')


def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Номер телефона']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list


def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по фамилии\n2 - по имени\n3 - по номеру телефона\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите фамилию для поиска: ')
        print()
    elif search_field == '2':
        search_value = input('Введите имя для поиска: ')
        print()
    elif search_field == '3':
        search_value = input('Введите номер для поиска: ')
        print()
    return search_field, search_value


def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, phone_number


def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')


def show_phonebook(file_name):
    list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
    print_contacts(list_of_contacts)
    print()
    return list_of_contacts


def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def change_phone_number(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()


if __name__ == '__main__':
    file = 'Phonebook.txt'
    choose_action(file)

# file_fon = 'C:/Users/Марс/PycharmProjects/pythonProject/lesson8/fon.txt'
# with open(file_fon, 'r+') as f:
#     # f = open('workfile', 'w', encoding="utf-8")
#     text = f.readlines()
#     fio = input("Ведите ФИО ")
#     tel = input("Ведите телефон ")
#     if fio not in text:
#        f.write(f"{fio} ,  {tel}\n")
#     else:
#         print("Человек с таким именем уже введен в телефонный справочник")
