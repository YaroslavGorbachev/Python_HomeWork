# # Задание 1:Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# import os
# os.system('cls')

# from hashlib import new
# from ntpath import join

# line = 'олрабв читсм абвопьп мгнеп попабвщршр мтпо'
# print(line)
# str = line.split() # Разделили строку на подстроки
# print(str)
# for elem in str:
#     if elem.find('абв') != -1:
#         str.remove(elem) # Удаление элементов, содержащих - абв
# print(str)            
# newline = ' '.join(str) # Сбор искомой строки
# print(newline)  


# # Задание 2:Создайте программу для игры с конфетами человек против человека.
# import os
# os.system('cls')
# from random import randint

# def lotteri ():
#     name11 = (input('Ведите имя первого игрока: '))
#     name1 = name11.upper()
#     a1 = randint(1,6) 
#     name22 = input('Ведите имя второго игрока: ')
#     name2 = name22.upper()
#     a2 = randint(1,6)
#     if a1 > a2:      
#         print ('Первый ход за игроком', name1,', которому выпала кость с номером', a1)
#         print ('Второй ход за игроком', name2,', которому выпала кость с номером', a2)
#         return name1, name2
#     elif a2 > a1:
#         print ('Первый ход за игроком', name2,', которому выпала кость с номером', a2)
#         print ('Второй ход за игроком', name1,', которому выпала кость с номером', a1)
#         return name2, name1
#     else:
#         print(name1,' -', a1,"  ", name2, ' -',a2, 'результаты равны, бросаем кости вновь'  )
#         lotteri()   

# def make_move (igrok, count, max):
#     print('\n', igrok, ', ваш ход.')
#     a = logika(count,max) 
#     while True:
#         player = (int(input('Выбранное количество конфет: ')))
#         if  player < 0 or player > max:   
#             print('Ваше число не в заданном диапазоне. Попробуйте снова')
#         elif player > count:
#             print('Выбранное число больше остатка конфет. Попробуйте снова')
#         else:
#             count = count - player   
#             print('Осталось ',count,' конфет')
#             break
#     return count, player 
  
# def logika (candi_l, max_l):
#     first_move = candi_l % (max_l + 1)
#     print ('(Для выигрыша необходимо взять ', first_move, ' конфет)')
#     return first_move

# print('УСЛОВИЕ ЗАДАЧИ: На столе лежит 2021 конфета.\nЗа один ход можно забрать до 28 кофет.')
# print('Все конфеты оппонента достаются сделавшему последний ход.')
# print('Жеребьевка проводится путем бросания костей с цифрами от 1 до 6.\n')

# igrok1, igrok2 = lotteri()
# candi = 2021
# max_candi = 28
# candi_igrok1, candi_igrok2 = 0, 0

# while candi != 0:
#     candi, coun_player1 = make_move (igrok1, candi, max_candi) 
#     candi_igrok1 = candi_igrok1 + coun_player1
#     if candi == 0:
#         print('Выиграл игрок ', igrok1,', которому возвращаются от оппонента', candi_igrok2, ' конфет')
#     else:
#         candi, count_player2 = make_move(igrok2, candi, max_candi)
#         candi_igrok2 = candi_igrok2 + count_player2
#         if candi == 0:
#             print('Выиграл игрок ', igrok2, ', которому возвращаются от оппонента', candi_igrok1, ' конфет')

# # Задание 3:Создайте программу для игры в ""Крестики-нолики"

# print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)
# board = list(range(1,10))
# def draw_board(board):
#    print("-" * 13)
#    for i in range(3):
#       print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#       print("-" * 13)
# def take_input(player_token):
#    valid = False
#    while not valid:
#       player_answer = input("Куда поставим " + player_token+"? ")
#       try:
#          player_answer = int(player_answer)
#       except:
#          print("Некорректный ввод. Вы уверены, что ввели число?")
#          continue
#       if player_answer >= 1 and player_answer <= 9:
#          if(str(board[player_answer-1]) not in "XO"):
#             board[player_answer-1] = player_token
#             valid = True
#          else:
#             print("Эта клетка уже занята!")
#       else:
#         print("Некорректный ввод. Введите число от 1 до 9.")
# def check_win(board):
#    win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
#    for each in win_coord:
#        if board[each[0]] == board[each[1]] == board[each[2]]:
#           return board[each[0]]
#    return False
# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#            take_input("X")
#         else:
#            take_input("O")
#         counter += 1
#         if counter > 4:
#            tmp = check_win(board)
#            if tmp:
#               print(tmp, "Вы выиграли!")
#               win = True
#               break
#         if counter == 9:
#             print("Ничья!")
#             break
#     draw_board(board)
# main(board)
# input("Нажмите Enter для выхода!")



# # Задание 4:Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('file_encode.txt', 'w') as data:
#     data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')

# with open('file_encode.txt', 'r') as data:
#     string = data.readline()

# def rle_encode(decoded_string):
#     encoded_string = ''
#     count = 1
#     char = decoded_string[0]
#     for i in range(1, len(decoded_string)):
#         if decoded_string[i] == char:
#             count += 1
#         else:
#             encoded_string = encoded_string + str(count) + char
#             char = decoded_string[i]
#             count = 1
#             encoded_string = encoded_string + str(count) + char
#     return encoded_string

# def rle_decode(encoded_string):
#     decoded_string = ''
#     char_amount = ''
#     for i in range(len(encoded_string)):
#         if encoded_string[i].isdigit():
#             char_amount += encoded_string[i]
#         else:
#             decoded_string += encoded_string[i] * int(char_amount)
#         char_amount = ''
#     print(decoded_string)

#     return decoded_string

# with open('file_encode.txt', 'r') as file:
#     decoded_string = file.read()

# with open('file_decode.txt', 'w') as file:
#     encoded_string = rle_encode(decoded_string)
#     file.write(encoded_string)

# print('Decoded string: \t' + decoded_string)
# print('Encoded string: \t' + rle_encode(decoded_string))
# print(f'Compress ratio: \t{round(len(decoded_string) / len(encoded_string), 1)}')