# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# 5 -> 1 0 1 1 0
# 2

# n = int(input("Введите кол-во монеток: "))
# count = 0
# max_count_1 = 0
# max_count_2 = 0
# for i in range(n):
#     temp = int(input("Введите какой стороной лежат монетки (1 или 0): "))
#     if temp == 0:
#         max_count_1 += 1
#     if temp == 1:
#         max_count_2 += 1
#     if max_count_1 > max_count_2:
#         print(max_count_2)
#     if max_count_2 > max_count_1:
#         print(max_count_1) 
    

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# 4 4 -> 2 2
# 5 6 -> 2 3

# s = int(input("Введите подсказку - сумму загаданных чисел : "))
# p = int(input("Введите подсказку - произведение загаданных чисел : "))
# X = s + p
# Y = s * p
# print(X,Y)


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

# n = int(input('Введите число n: '))
# k = 0
# res = 1
# while res < n+1:
#     print(res, end=' ')
#     k += 1
#     res = 2 ** k