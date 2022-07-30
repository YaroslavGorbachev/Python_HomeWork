# # #Задание 1:Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Было
# # n = [2, 3, 5, 9, 3]
# # sum = 0 
# # for i in range(1,len(n),2):
# #     if i % 2 == 1:
# #         sum = sum + int(n[i])

# Стало
# list = [2, 3, 5, 9, 3]
# list2 = [ list[i] for i in range(1, len(list), 2)]  
# print(sum(list2))


# # # #Задание 2:Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Было
# # import math
# # n = [2, 3, 5, 6]
# # # n = [2, 3, 4, 5, 6]
# # result = []
# # for i in range(math.ceil(len(n)/2)): 
# #     result.append(int(n[i])*int(n[len(n)-1-i]))
# # print(result)

# Стало
# list = [2, 3, 5, 6]
# list = [2, 3, 4, 5, 6]
# list2 = [list[i]*list[-i-1] for i in range((len(list)+1)//2)]
# print(list2)

# #Задание 2:Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# Было
# n = int(input("введите число: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial)
# # Стало


# from math import factorial

# n = int(input('Введите число: '))
# f = lambda x: ((x == 1) and 1) or x * factorial(x -1)
# list2 = list( f(i) for i in range(1, n +1))
# print(list2)

