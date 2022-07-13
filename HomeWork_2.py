# #Задание 1:Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n = input("введите число: ")
# suma = 0
# for digit in n:
#     if digit.isdigit():
#         suma += int(digit)
# print("Сумма:", suma)


# #Задание 2:Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# n = int(input("введите число: "))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial)


# #Задание 3:Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# # (1+1/n)**n,

# n = int(input("число: "))
# sum=0
# i=1
# while i<=n:
#     s=(1+1/i)**i
#     print(s)
#     sum +=s
#     i=i+1
# print(sum)


#Задание 4:Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях.
#Позиции хранятся в файле file.txt в одной строке одно число

# первый пример решения РАБОТАЕТ
# from random import randint
# num = 6
# lst = []
# for i in range(-num, num, 2):
#     lst.append(randint(-num, num))
# print(lst)
# with open('E:\Python\HomeWork\\file.txt', 'r') as data:
#     ind = data.read()
# result = 1
# for j in ind.split('\n'):
#     result *= lst[int(j)]
#     print(int(j))
# print(result)

# второй пример решения Ошибка никак не смог решить ее
# f = open('text.txt','w')
# for i in 1,3,5:
#     f.write(str(i))
#     int("10")
#     10
#     type(int("10"))
# f.close()
# with open('text.txt', 'r') as data:
#     ind = data.read()
# result = 1
# for j in ind.split('\n'):
#     result *= lst[int(j)]
#     print(int(j))
# print(result)


# # Задание 5:Реализуйте алгоритм перемешивания списка.
# import random
 
# y = ['123', 'кот ', '254', 'человек']
# print(y)
# random.shuffle(y)
# print(y)