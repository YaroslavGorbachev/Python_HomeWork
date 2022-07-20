# #Задание 1:Вычислить число c заданной точностью d
# import math
# n = int(input('Введите количество цифр после запятой: '))
# print('Число 𝜋: {:.50f}'.format(math.pi))
# a = math.pi
# b = round(a,n+1)*10**n
# c = math.modf(b)
# a = c[1] / 10**n
# print('Число 𝜋 с заданной точностью:',a)


# #Задание 2:Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

# n=int(input("Integer: ")) 
# factors = []
# d = 2
# m = n 
# while d * d <= n:
#         if n % d == 0:
#             factors.append(d)
#             n//=d
#         else:
#             d += 1
# factors.append(n)
# print('{} = {}' .format(n,factors))


# #Задание 3:Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# a = [1, 2, 2, 3, 4, 6, 8, 8, 2, 9, 7, 4, 9]
# i = a[0]
# c = []
# for i in a:
#     if i in c:
#        continue
#     else:
#        c.append(i)
# print(c)


# #Задание 4:Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# #многочлена и записать в файл многочлен степени k.

# import itertools
# k = randint(2, 8)
# def get_ratios(k):
#     ratios = [randint(0, 100) for i in range (k + 1)]
#     while ratios[0] == 0:
#         ratios[0] = randint(1, 100) 
#     return ratios
# def get_polynomial(k, ratios):
#     var = ['*x^']*(k-1) + ['*x']
#     polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(ratios, var, range(k, 1, -1), fillvalue = '') if a !=0]
#     for x in polynomial:
#         x.append(' + ')
#     polynomial = list(itertools.chain(*polynomial))
#     polynomial[-1] = ' = 0'
#     return "".join(map(str, polynomial)).replace(' 1*x',' x')
# ratios = get_ratios(k)
# polynom1 = get_polynomial(k, ratios)
# print(polynom1)
# with open('file.txt, 'w') as data:
#     data.write(polynom1)

# #Задание 5:Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# from itertools import *
# from Task033 import get_polynomial
# import os
# os.system("cls")

# file1 = 'file.txt.txt'
# file2 = 'file_2.txt'
# def read_pol(file): 
#     with open(str(file), 'r') as data:
#         pol = data.read()
#     return pol
# def convert_pol(pol):  
#     pol.replace('= 0', '')
#     pol = pol.split(' + ')
#     pol = [i[0] for i in pol]
#     for i in range(len(pol)):
#         if pol[i] == 'x':
#             pol[i] = '1'
#     pol = pol[::-1]
#     return pol
# pol1 = read_pol(file1)
# pol2 = read_pol(file2)
# print('Исходные полиномы:')
# print(pol1)
# print(pol2)
# print('_'*30)
# print(convert_pol(pol1))
# print(convert_pol(pol2))
# pol1_coef = list(map(int, convert_pol(pol1)))
# pol2_coef = list(map(int, convert_pol(pol2)))
# print(pol1_coef)
# print(pol2_coef)
# print('_'*30)
# sum_coef = list(map(sum, zip_longest(pol1_coef, pol2_coef, fillvalue=0)))
# print(sum_coef)
# sum_coef = sum_coef[::-1]
# print(sum_coef)
# sum_pol = get_polynomial(len(sum_coef)-1, sum_coef)
# print('Итоговый результат сложения полиномов:\n', sum_pol)
# with open('task034.txt', 'w') as file_sum:
#     file_sum.writelines(sum_pol)