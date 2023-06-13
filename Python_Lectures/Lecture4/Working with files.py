# Работа с файлами в Python:
# ///////////////////////////////////////////////////////////////////////////////////
# Содержание:
# 1. Введение в тему
# 2. Файлы python
# 3. Текстовые файлы
# 4. Бинарные файлы
# 5. Открытие файла
#       5.1 Метод open
#       5.2 Пример
# 6. Закрытие файла
#       6.1 Метод close
#       6.2 Инструкция with
# 7. Чтение и запись файлов в python
#       7.1 Функция read
#       7.2 Функция readline
#       7.3 Функция write
# 8. Переименование файлов в python
# 9. Функция rename
# 10.Текущая позиция в файлах python
# ///////////////////////////////////////////////////////////////////////////////////

# 1. Введение в тему.

#   В данном уроке мы рассмотрим работу с файлами в Python.
# Вы узнаете, как их открывать, читать содержимое, вносить изменения и закрывать их.

# ///////////////////////////////////////////////////////////////////////////////////

# 2. Файлы python.

#   Файл — это определенное количество информации, имеющее имя и хранящееся в долговременной памяти.
# Другими словами, это набор данных, которому дали имя и где - то сохранили.
#   В Питоне файлы делятся на две разновидности:
# — Текстовые
# — Бинарные

# ///////////////////////////////////////////////////////////////////////////////////

# 3. Текстовые файлы.

#   Предполагается, что этот вид файлов содержит набор символов, который может прочитать человек.
# Как правило, такие файлы могут быть открыты любым простейшим текстовым редактором, к примеру, блокнотом в Виндовс.

# ///////////////////////////////////////////////////////////////////////////////////

# 4. Бинарные файлы.

#   Бинарные файлы содержат набор нулей и единиц.
# Таким образом можно хранить любую информацию: изображения, аудио, видео и даже текст.
#   Работа с файлами состоит из следующих шагов:
# - Файл надо открыть
# - Произвести необходимые операции (запись или чтение)
# - Закрыть файл

# ///////////////////////////////////////////////////////////////////////////////////

# 5. Открытие файла.

# ///////////////////////////////////////////////////////////////////////////////////

#   5.1 Метод open.

#   И так, если Вы хотите произвести какие - либо операции с файлом, сперва придётся его открыть.
# Для этой цели в языке Пайтон есть встроенная функция open().
# Используя эту функцию, можно создать на основе любого языка файла объект Python.

# file = open(name, mode) где,

# name - имя файла, который Вы открываете
# mode - режим открытия. Если не указать этот параметр, файл будет открыт в режиме «только чтение».

# Режимы открытия файла могут быть следующими:

# (r)    Режим только для чтения. Указать стоит в начале файла.
# (a)	 Режим для добавления информации в файл. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.
# (a +)  Режим для добавления и чтения. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.
# (ab)	 Режим для добавления в двоичном формате. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.
# (ab +) Режим для добавления и чтения в двоичном формате. Указатель стоит в конце файла. Создает файл с именем имя_файла, если такового не существует.
# (r +)  Режим для чтения и записи. Указатель стоит в начале файла.
# (rb)	 Режим для чтения в двоичном формате. Указатель стоит в начале файла.
# (rb +) Режим для чтения и записи в двоичном формате. Указатель стоит в начале файла.
# (w)	 Режим только для записи. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
# (w +)  Режим для чтения и записи. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
# (wb)	 Режим для записи в двоичном формате. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.
# (wb +) Режим для чтения и записи в двоичном формате. Указатель стоит в начале файла. Создает файл с именем имя_файла, если такового не существует.

#   Файловый объект имеет несколько атрибутов, предоставляющих информацию о файле:

# file.closed       Выводит True, если файл был закрыт.
# file.mode	        Выводит режим доступа, с которым был открыт файл.
# file.name	        Выводит имя файла.
# file.softspace	Выводит False, если при выводе содержимого файла следует отдельно добавлять пробел.

# ///////////////////////////////////////////////////////////////////////////////////

#   5.2 Пример.

#   Для начала необходимо сохранить в новый файл «test.txt» какой - то текст.
# Этот файл должен быть расположен в рабочей папке.

#   Применим следующий код для открытия данного файла:
# path = 'test.txt'
# file = open(path, 'r', encoding='utf-8')  # открыть файл из рабочей папки в режиме чтения, относительный путь
# for line in file:
#     print(line)  # вывели текст из файла
# file.close()  # используется для закрытия файла, чтобы разорвать подключение файловой переменной с файлом на диске.
# file_2 = open('C:\\Users\\nagovitsin\Desktop\\CourseProgrammerSpecialization\\test_2.txt', 'r', encoding='utf-8')  # открыть файл из любого каталога
# for line in file_2:
#     print(line)
# file_2.close()
# В переменных file и file_2 хранятся ссылки на объекты с открытыми файлами.

# Теперь посмотрим содержимое файла и информацию о нём:

file = open('C:\\Users\\nagovitsin\Desktop\\CourseProgrammerSpecialization\\test.txt', 'r', encoding='utf-8')
print(*file)  # вывод текста из файла
print(file)  # информация о файле
file.close()
# Вывод:
# Аристотель: "Свободный человек — тот, который существует ради себя, а не ради другого."

# < _io.TextIOWrapper name = 'C:\\Users\\nagovitsin\\Desktop\\CourseProgrammerSpecialization\\test.txt' mode = 'r' encoding = 'utf-8' >

# ///////////////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////
# /////////////// Лекция 4 /////////////

# Файлы в текстовом формате используются для:
# ● Хранения данных
# ● Передачи данных в клиент - серверных проектах
# ● Хранения конфигов
# ● Логирования действий

# Что нужно для работы с файлами:
# 1. Завести переменную, которая будет связана с этим текстовым файлом.
# 2. Указать путь к файлу.
# 3. Указать, в каком режиме мы будем работать с файлом.

# Варианты режима (мод):
# Режим:	Описание:
# r	    Только для чтения.
# w	    Только для записи. Создаст новый файл, если не найдет с указанным именем.
# rb	Только для чтения (бинарный).
# wb	Только для записи (бинарный). Создаст новый файл, если не найдет с указанным именем.
# r + 	Для чтения и записи.
# rb + 	Для чтения и записи (бинарный).
# w + 	Для чтения и записи. Создаст новый файл для записи, если не найдет с указанным именем.
# wb + 	Для чтения и записи (бинарный). Создаст новый файл для записи, если не найдет с указанным именем.
# a	    Откроет для добавления нового содержимого. Создаст новый файл для записи, если не найдет с указанным именем.
# a + 	Откроет для добавления нового содержимого. Создаст новый файл для чтения записи, если не найдет с указанным именем.
# ab	Откроет для добавления нового содержимого (бинарный). Создаст новый файл для записи, если не найдет с указанным именем.
# ab + 	Откроет для добавления нового содержимого (бинарный). Создаст новый файл для чтения записи, если не найдет с указанным именем.

# a – открытие для добавления данных.
# ○ Позволяет дописывать что-то в имеющийся файл.
# ○ Если вы попробуете дописать что-то в несуществующий файл, то файл будет создан и в него начнется запись.

# r – открытие для чтения данных.
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
# 2. Режим r (readlines) (r – открытие для чтения данных)

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
