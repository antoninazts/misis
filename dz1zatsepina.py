# 1 Языки программирования для работы с данными. Семенычев Артем
# дз1 Зацепина Антонина

import math
import re

# # Задача 1. Сумма первых n положительных чисел
# # Напишите программу, запрашивающую у пользователя число и подсчитывающую сумму натуральных
# # положительных чисел от 1 до введенного пользователем значения. Сумма первых n положительных чисел
# # может быть рассчитана по формуле:
# # sum = n * (n + 1)2
# print("Задача 1. Сумма первых n положительных чисел")
# n = int(input("Введите число: "))
# sum = n * (n + 1)/2
# print('Сумма первых {} положительных чисел = {}'.format(n, sum))


# # Задача 2. Калькулятор
# # Составьте программу, которая запрашивает у пользователя 2 целых числа и выполняет операции:
# # арифметические: +, -, * , / , // , %, **, log10;
# # сравнение: <, <=, >, >=, !=, ==,
# # выводя на экран результат каждого действия. В случае получение вещественного результата, округлите
# # его до 2-х знаков после запятой (используя функцию round()).
# # Подсказка. Функцию log10 вы найдете в модуле math.
# print("Задача 2. Калькулятор")
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# print("арифметические операции:")
# print("{} + {} = {}".format(a, b, a + b))
# print("{} - {} = {}".format(a, b, a - b))
# print("{} * {} = {}".format(a, b, a * b))
# print("{} / {} = {}".format(a, b, round(a / b, 2)))
# print("{} // {} = {}".format(a, b, a // b))
# print("{} % {} = {}".format(a, b, a % b))
# print("{} ^ {} = {}".format(a, b, a ** b))
# print("log10{} = {}".format(a, round(math.log10(a)), 2))
# print("log10{} = {}".format(b, round(math.log10(b), 2)))
# print("сравнение:")
# print("{} < {} = {}".format(a, b, a < b))
# print("{} <= {} = {}".format(a, b, a <= b))
# print("{} > {} = {}".format(a, b, a > b))
# print("{} >= {} = {}".format(a, b, a >= b))
# print("{} != {} = {}".format(a, b, a != b))
# print("{} == {} = {}".format(a, b, a == b))


# # Задача 3.
# # Вычислите значение следующего выражения (аргументы - целые числа и вводятся с клавиатуры):
# f = 3x5 + 7|-6|  y7 - zmody
# Округлите результат до 3-х знаков после запятой, используя функцию round().
# print("Задача 3.")
# x = int(input("x = "))
# y = int(input("y = "))
# z = int(input("z = "))
# rez = round((((x**5+7)/(abs(-6)*y))**(1/3))/(7-z%y), 3)
# print("rezult  = {}".format(rez))


# # Задача 4.
# # Дана электрическая цепь, состоящая из 2-х последовательно соединенных проводников (сопротивление
# # каждого известно). Найти общее сопротивление цепи (округление результата необходимо выполнить до
# 1-го знака после запятой).
# print("Задача 4.")
# r1 = float(input("R1 = "))
# r2 = float(input("R2 = "))
# r = round(r1+r2, 1)
# print("R общее  = {}".format(r))


# # Задача 5.
# # Дано уравнение ax + b = 0 и отрезок [m;n]. Ответьте на вопрос, попадает ли решение уравнения в
# # указанный отрезок.
# print("Задача 5.")
# a = float(input("a = "))
# b = float(input("b = "))
# m = float(input("m = "))
# n = float(input("n = "))
# x = -b / a
# if x >= m and x <= n:
#     print("x = {} в отрезок [{};{}] попал".format(x, m, n))
# else:
#     print("x = {} в отрезок [{};{}] не попал".format(x, m, n))

# # Задача 6. Поездка по кругу
# # Спортсмен решил потренироваться перед марафоном и покататься вокруг города на скорость. Длина
# # дороги — 123 километра. Спортсмен стартует с нулевого километра и едет со скоростью v километров
# # в час. На какой отметке он остановится через t часов?
# # Реализуйте программу, которая спрашивает у пользователя v и t и выводит целое число от 0 до 122 —
# # номер километра, на котором остановится Спортсмен. Учтите, что он может прокатиться больше одного
# # круга.
# print("Задача 6. Поездка по кругу")
# max_s = 123
# v = float(input("v = "))
# t = float(input("t = "))
# s = int((v * t) % (max_s - 1))
# print("Остановился на {} км".format(s))

# # Задача 7. Сумма и произведение цифр в числе
# # Дано двузначное и трехзначное число. Для каждого выведите на экран сумму и произведение цифр.
# # print("Задача 7. Сумма и произведение цифр в числе")
# a = list(input("a = "))
# sum = 0
# m = 1
# for i in range(len(a)):
#     b = int(a[i])
#     sum += b
# print("Сумма цифр в числе =", sum)
# for i in range(len(a)):
#     b = int(a[i])
#     m *= b
# print("Произведение цифр в числе =", m)

# # Задача 8. Сортировка трех чисел
# # Напишите программу, запрашивающую у пользователя три целых числа и выводящую их в упорядоченном
# # виде – по возрастанию. Используйте функции min и max для нахождения наименьшего и наибольшего
# # значений. Оставшееся число можно найти путем вычитания из суммы трех введенных чисел
# # максимального и минимального.
# print("Задача 8. Сортировка трех чисел")
# n1 = int(input("n1 = "))
# n2 = int(input("n2 = "))
# n3 = int(input("n3 = "))
# a = (n1, n2, n3)
# min = min(a)
# max = max(a)
# middle = sum(a) - min - max
# print(min, middle, max)


# # Задача 9. Поменять местами: не всё так просто!
# # Напишите программу, которая меняла бы значения двух переменных местами, но без использования
# # третьей переменной и синтаксического сахара, а именно — без конструкции
# # a, b = b, a
# # В переменные будут вводиться только числа.
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# print(a, b)
# a = a + b
# b = a - b
# a = a - b
# print(a, b)


# # Задача 10.
# # Составьте программу, которая запрашивает название футбольной команды и повторяет его на экране со
# # словами ... - чемпион!
# # После этого выполните:
# # используя операцию дублирования, нарисуйте черту (набор "-"), длиной, равной размеру названия
# # команды;
# # преобразуйте строку в нижний регистр и выведите на экран:
# # длину наименования команды;
# # есть ли в наименовании команды буква "п" (True/False)?
# # сколько раз повторяется буква "а"?
# c = input('Введите футбольную команду: ')
# print("{} - чемпион!".format(c))
# print("-" * len(c))
# c = c.lower()
# print(c)
# print(len(c))
# print(c.find("п") != -1)
# print(c.count("а"))

# # Задача 11.
# # Составьте программу, которая запрашивает название государства и его столицы, а затем выводит
# # сообщение:
# # Государство - ..., столица - ...
# # На месте многоточий должны быть выведены соответствующие значения.
# print("писать через пробел")
# a = list(input("Государствa: ").split(" "))
# b = list(input("столицы: ").split(" "))
# if len(a) == len(b):
#     for i in range(len(a)):
#         print(f"Государство - {a[i]}, столица - {b[i]}\n")
# else:
#     print("количество государств и столиц не совпадает")

# # Задача 12.
# # Дано слово объектно-ориентированный. Используя индексацию и срезы составьте из него слова объект,
# # ориентир, тир, кот, рента и выведите их на экран.
# a = str("объектно-ориентированный")
# print(a)
# print(a[:6])
# print(a[9:17])
# print(a[14:17])
# print(f"{a[4]}{a[0]}{a[5]}")
# print(f"{a[10]}{a[12:15]}{a[19]}")


# # Задача 13.
# # Создайте 2 пустых списка и выполните операции, описанные в заготовке.
# #
# # Создать 2 пустых списка
# a = list()
# b = list()
#
# # Добавить 2 вещественных числа (4.5 и 3.4) в список 'a' с помощью append
# a.append(4.5)
# a.append(3.4)
# # Добавить 2 вещественных числа (8.7, 1.3) в список 'a' с помощью extend
# a.extend([8.7, 1.3])
#
# # Добавить 2 вещественных числа (14.5, 3.4) в список 'b' с помощью append
# b.append(14.5)
# b.append(3.4)
#
# # Добавить 2 вещественных числа (8.7, 11.3) в список 'b'с помощью extend
# b.extend([8.7, 11.3])
#
# # Вставить целое число 100 на 2-е и 4-е место списка 'a'
# a.insert(1, 100)
# a.insert(3, 100)
#
# # Вставить целое число 200 на 1-е и 3-е место списка 'b'
# b.insert(0, 200)
# b.insert(2, 200)
#
# # Вывести списки на экран
# print("Исходные списки:")
# print(*a)
# print(*b)
#
# # Удалить первые элементы из списков 'a' и 'b'
# del a[0]
# del b[0]
#
# # Удалить элемент 100 из списка 'a'
# a.remove(100)
# # Удалить элемент 200 из списка 'b'
# b.remove(200)
#
# # Вывести списки на экран
# print("\nПосле удалений:")
# print(*a)
# print(*b)
#
# # Создать множества из списков 'a' и 'b', а также их пересечение
# sa = set(a)
# sb = set(b)
# sa_and_sb = sa & sb
# # Вывести экран уникальные элементы каждого списка и общие
# print("\nУникальные элементы:")
# # Удалите комментарий и допишите код
# print("общие:", sa_and_sb)
#
# # Соединить списки 'a' и 'b'
# c = a + b
#
# # Отсортировать список 'c' по возрастанию и убыванию
# c_asc = sorted(c)
# c_desc = sorted(c, reverse=True)
#
# # Среднее арифметическое элементов списка 'c', расположенных на четных местах
# even = c[1::2]
# sr_ar =  sum(even)/len(even)
# # Среднее геометрическое элементов списка 'c', расположенных на нечетных местах
# odd = c[::2]
# sr_geom =  math.prod(odd)**(1/len(odd))
#
# # Максимальный и минимальный элементы
# c_max = max(c)
# c_min = min(c)
#
# # Вывести результаты на экран
# print("\nИтоговые:")
# print("3-й:", c)
# print("Сортировка (возр.): ", c_asc)
# print("Сортировка (убыв.): ", c_desc)
# print(f"Ср. арифм. = {sr_ar}, ср. геометр. = {round(sr_geom, 2)}")
# print("Макс. и мин.:", c_max, c_min)

# # --------------
# # Пример вывода:
# #
# # Исходные списки:
# # 1-й: [4.5, 100, 3.4, 100, 8.7, 1.3]
# # 2-й: [200, 14.5, 200, 3.4, 8.7, 11.3]
# #
# # После удалений:
# # 1-й: [3.4, 100, 8.7, 1.3]
# # 2-й: [14.5, 3.4, 8.7, 11.3]
# #
# # Уникальные элементы:
# # 1-й: {8.7, 1.3, 3.4, 100}
# # 2-й: {8.7, 11.3, 3.4, 14.5}
# # общие: {8.7, 3.4}
#
# # Итоговые:
# # 3-й: [3.4, 100, 8.7, 1.3, 14.5, 3.4, 8.7, 11.3]
# # Сортировка (возр.): [1.3, 3.4, 3.4, 8.7, 8.7, 11.3, 14.5, 100]
# # Сортировка (убыв.): [100, 14.5, 11.3, 8.7, 8.7, 3.4, 3.4, 1.3]
# # Ср. арифм. = 29.00, ср. геометр. = 7.82
# # Макс. и мин.: 100 1.3


# # Задача 14.
# # Создайте пустой словарь для хранения информации о себе и выполните операции, описанные в
# # заготовке.
# # В данной задаче все значения задаются в коде (без input())
#
# # 1. Создание словаря
# # Создать пустой словарь
# info = dict()
#
# # Добавить значения для ключей "фио", "дата_рождения", "место_рождения"
# info["фио"] = "Зацепина Антонина"
# info["дата_рождения"] = "23.09.1995"
# info["место_рождения"] = "Москва"
#
# # Напечатать словарь
# print(info)
#
# # Создать ключ "хобби" со значением = список из строк -
# # наименований хобби (например "плавание" и т.д.)
# info["хобби"] = ["спорт", "музыка"]
#
# # Добавить "программирование" в список хобби
# info["хобби"].append("программирование")
#
# # Создать ключ "животные" со значением = кортеж из строк -
# # имен домашних животных (например "кошка Мурка" и т.д.)
# info["животные"] = ("кошка Мурка", "собака Жучка")
#
# # Создать ключ "ЕГЭ" и поместить в него пустой словарь
# info["ЕГЭ"] = {}
#
# # В словарь info["ЕГЭ"] добавить информацию о сданных экзаменах,
# info["ЕГЭ"]["математика"] = 100
# info["ЕГЭ"]["русский"] = 99
# info["ЕГЭ"]["физика"] = 98
#
# # Добавить экзамен, который не был сдан, после чего удалить его
# info["ЕГЭ"]["информатика"] = "не сдан"
# # print(info)
# del info["ЕГЭ"]["информатика"]
# # print(info)
#
# # Создать ключ "вузы" и поместить в него пустой словарь
# info["вузы"] = {}
#
# # В словарь info["вузы"] добавить информацию о вузах,
# # где ключ - аббревиатура вуза, а значение -
# # количество баллов для специальности, на которую хотели поступить
# info["вузы"]["AAA"] = 90
# info["вузы"]["BBB"] = 80
# # print(info)
#
#
# # 2. Вывод на экран
# print("Данные:")
# print(info)
#
# # Список экзаменов ЕГЭ в алфавитном порядке
# # (используйте метод ``keys()``, преобразовав результат в кортеж)
# exams = info["ЕГЭ"].keys()
# print("Предметы:", *exams)
# # Список вузов в алфавитном порядке
# uni = info["вузы"].keys()
# print("Вузы:", *uni)
#
# # 3. Ответы на вопросы
# print("\nОтветы на вопросы:")
#
# # Выделить имя из info["фио"]
# name = re.findall(r"[ ](\w+)", info["фио"])
# print(*name)
# # Начинается на гласную? (True/False)
# starts_with_vowel = bool(re.search(r"^(?i:[аеёиоуыэюя])", *name))
# print("* мое имя начинается на гласную букву:", starts_with_vowel)
#
# # Выделить месяц из info["дата_рождения"]
# month = re.findall(r"\.(\d\d)\.", info["дата_рождения"])
# print(*month)
# # Родился зимой или летом? (True/False)
# born_in_winter_or_summer = bool(re.search(r"0[67812]|[12]", *month))
# print("* родился летом или зимой:", born_in_winter_or_summer)
#
# # Количество хобби и первое из них
# hobbies_count = len(info["хобби"])
# print("* у меня {} хобби, первое \"{}\"".format(hobbies_count, info["хобби"][0]))
#
# # Количество сданных экзаменов
# exams_count = len(exams)
# print("* после окончания школы сдавал {} экз.".format(exams_count))
#
# # Сумма баллов по экзаменам
# sum_mark = sum(info["ЕГЭ"].values())
# print("* сумма баллов = {}".format(sum_mark))
#
# # Максимальный балл среди сданных
# max_mark = max(info["ЕГЭ"].values())
# print("* макс. балл = {}".format(max_mark))
#
# # Количество вузов, в которые Вы проходите по баллам
# # Подсказка: определить, проходите Вы или нет, можно простым сравнением
# # суммы баллов с проходным баллом вуза - ``True/False``.
# # Для того, чтобы определить количество таких вузов, преобразуйте
# # сравнение в целое число (используя ``int()``) и сложите все сравниваемые вузы.
# vuz_count = sum(i <= sum_mark for i in info["вузы"].values())
# print("* кол-во вузов в которые прохожу: {}".format(vuz_count))

# # --------------  # # Пример вывода:  # #  # # {'фио': 'Иванов Иван Иванович', 'место_рождения': 'Париж',  # #  'дата_рождения': '01/09/1995'}  # # Данные:  # # {'фио': 'Иванов Иван Иванович', 'животные': ('кошка Мурка',),  # #  'вузы': {'МИРЭА': 240, 'МГУ': 295, 'МГТУ им. Баумана': 255},  # #  'хобби': ['игра на гитаре', 'туризм', 'программирование'],  # #  'ЕГЭ': {'Математика': 90, 'Информатика': 88, 'Русский язык': 67},  # #  'дата_рождения': '01/09/1995', 'место_рождения': 'Париж'}  # # Предметы: Информатика, Математика, Русский язык  # # Вузы: МГТУ им. Баумана, МГУ, МИРЭА  #  # # Ответы на вопросы:  # # * мое имя начинается на гласную букву: True  # # * родился летом или зимой: False  # # * у меня 3 хобби, первое "игра на гитаре"  # # * после окончания школы сдавал 3 экз.  # # * сумма баллов = 245  # # * макс. балл = 90  # # * кол-во вузов в которые прохожу: 1  #  #  #
