# 30. Вычислить число c заданной точностью d
#     Пример:
#     - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi

# d = input('Введите число d: ')
# accuracy = len(d)
# print(str(pi)[0:accuracy])


# d = float(input('Введите число d: '))
# count = 0
# if 10 ** (-10) <= d <= 10 ** (-1):
#     while d < 1:
#         d = d * 10
#         count += 1
#     print(round(pi, count))
# else:
#     print('Неверный ввод')


# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input('Введите число N: '))
# some_list = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         for j in range(2, i // 2 + 1):
#             if i % j == 0:
#                 break
#         else:
#             some_list.append(i)
# print(some_list)


# 32. Задайте последовательность чисел. Напишите программу, которая выведет
#     список неповторяющихся элементов исходной последовательности.


# some_list = list(map(int, input().split()))
# for i in some_list:
#     if some_list.count(i) == 1:
#         print(i, end=' ')



