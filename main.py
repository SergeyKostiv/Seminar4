# import random
# import time
# 
# some_set = set()
# for _ in range(10 ** 6):
#     some_set.add(random.randint(100, 1100))
# some_list = list(some_set)
# 
# start = time.perf_counter()
# print(99 in some_list)
# end = time.perf_counter()
# first_duration = end - start
# 
# start = time.perf_counter()
# print(99 in some_set)
# end = time.perf_counter()
# second_duration = end - start
# print(first_duration / second_duration)



# some_dict = {'яблоко': 'apple', 'виноград': 'grape', 'банан': 'ban'}
# some_dict['банан'] = 'banana'
# print(some_dict['виноград'])

# for i in some_dict:
#     print(i, some_dict[i])

# for j in some_dict.values():
#     print(j)

# for i in sorted(some_dict):
#     print(i, some_dict[i])


'''
Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D,
G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова.
Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
либо только русские буквы.

*Пример:*

ноутбук
12
'''  

# scrabble_dict = {'A':1, 'E':1, 'I':1}
# some_str = input()
# summa = 0

# for letter in some_str:
#     summa += scrabble_dict[letter]
# print(summa)
# дописать код до конца



# 25. Напишите программу, которая принимает на вход строку,
# и выводит на экран кол-во повторений каждого из символов
# Пример
# Ввод: как дела
""" k - 2
    а - 2
    д - 1
    е - 1
    л - 1
"""

# string = input("Введите строку: ")
# counts = {} # Создаем словарь

# for letter in string:
#      if letter in counts:
#          counts[letter] += 1
# else:
#      counts[letter] = 1

# for letter, count in counts.items():
#    print("Символ '{}' повторяется '{}' раз(а)".format (letter, count))

# word = input() 
# used = set() 
# for letter in word:
#     if letter not in used:
#         print(f'{letter} - {word.count(letter)}')
#     used.add(letter)

# some_dict = {}
# word = input()
# for letter in word:
#     if letter not in some_dict:
#         some_dict[letter] = 1
# else:
#     some_dict[letter] += 1
# print(some_dict)

