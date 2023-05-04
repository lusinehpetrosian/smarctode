# 62
# from random import choice
# from time import sleep
# red = 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
# black = 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35
# green = '00' , '0'
# print('Which type of game do you want to play?\n1) Guess a number\n2) Guess a color\n3) Odd or even\n4) 1-18 or 19-36\n5) 0 or 00')
# type_of_game = int(input('Which type oof game do you wanna play(1-5)?\n>>>'))
# if type_of_game == 1: #guess a number
#     player_number = int(input('Guess a number(1-36)\n>>>'))
#     pc_number = choice(red + black)
#     if player_number == pc_number:
#         print('The winning bet is .....')
#         sleep(1)
#         print(pc_number)
#         print(f'{player_number}\nAnd you won!!!')
#     else:
#         print(f'The winning bet is .....')
#         sleep(1)
#         print(pc_number)
#         print(f'Next time:( ')
# elif type_of_game == 2: #guess a color
#     player_color = input('Guess a color(red or black)\n>> ')
#     pc_number = choice(red + black)
#     if pc_number in red and player_color == 'red':
#         print('The winning bet is .....')
#         sleep(1)
#         print(pc_number)
#         print(f'{player_color}\nAnd you won!!!')
#     elif pc_number in black and player_color == 'black':
#         print('The winning bet is .....')
#         sleep(1)
#         print(pc_number)
#         print(f'{player_color}\nAnd you won!!!')
#     else:
#         print(f'The winning bet is .....')
#         sleep(1)
#         print(pc_number)
#         print(f'Next time:( ')
# elif type_of_game == 3: #odd or even
#     player_thinks = input('Guess odd or even\n>>> ')
#     pc_number = choice(red + black)
#     if pc_number % 2 == 0 and player_thinks == 'even':
#         print('The winning bet is .....')
#         sleep(1)
#         print(pc_number)
#         print(f'{player_thinks}\nAnd you won!!!')
#     elif pc_number % 2 == 1 and player_thinks == 'odd':
#         print('The winning bet is .....')
#         sleep(1)
#         print(pc_number)
#         print(f'{player_thinks}\nAnd you won!!!')
#     else: 
#         print(f'The winning bet is .....')
#         sleep(1)
#         print(pc_number)
#         print(f'Next time:( ')
# elif type_of_game == 4: #1-18 or 19-36
#     player_thinks = input('1-18 or 19-36\n>>> ')
#     pc_number = choice(red + black)
#     if player_thinks == '1-18' and 1 <= pc_number <= 18:
#         print('The winning bet is .....')
#         sleep(1)
#         print(pc_number)
#         print(f'{player_thinks}\nAnd you won!!!')
#     elif player_thinks == '19-36' and 19 <= pc_number <= 36:
#         print('The winning bet is .....')
#         sleep(1)
#         print(pc_number)
#         print(f'{player_thinks}\nAnd you won!!!')
#     else: 
#         print(f'The winning bet is .....')
#         sleep(1)
#         print(pc_number)
#         print(f'Next time:( ')
# elif type_of_game == 5: #0 or 00 
#     player_choice = input('Guess 0 or 00: ')
#     pc_choice = choice(red + black + green)
#     if player_choice == '0' and pc_choice == '0':
#         print('You won!!!')
#     elif player_choice == '00' and pc_choice == '00':
#         print('You won!!!')
#     else:
#         print(pc_choice)
#         print('Next time :(')

#45
# date = input('Enter the date (month and day)\n>> ')
# ind = date.index(' ')
# month = date[:ind]
# day = date[ind+1:]
# # print(day,month)
# if month == 'january' and day == '1':
#     print("New Year's Day")
# elif month == 'july' and day == '1':
#     print('Canada Day')
# elif month == 'december' and day == '25':
#     print('Christmas Day')
# else:
#     print('There is no holiday this day!!')

# #46
# position = input('Enter the position (letter and digit)\n>>')
# if position[0] in 'aceg':
#     if int(position[1]) % 2 == 1:
#         print('black')
#     else:
#         print('white')
# elif position[0] in 'bdfh':
#     if int(position[1]) % 2 == 0:
#         print('black')
#     else:
#         print('white')  

# #47
# date = input('Enter the date (month then the day)')
# ind = date.index(' ')
# month = date[:ind]
# day = int(date[ind+1:])

# if (month == 'march' and 20 <= day <= 31) or month == 'april' or month == 'may' or (month == 'june' and 0 <= day < 20):
#     print('Spring')
# elif (month == 'september' and 0 <= day < 21) or (0<= day <= 30 and (month =='july' or month == 'august')) or (21 <=day <= 30 and month =='june'):
#     print('Summer')
# elif (0 <= day <= 30 and month == 'november') or (0 <=day <= 31 and month =='october') or (month == 'september' and 22 <= day < 30)  or (0 <= day <= 20 and month =='december'):
#     print('Autumn')
# elif (21 <= day <= 31 and month =='december') or (0 <= day <= 31 and month == 'january') or (0 <=day <= 29 and month =='february') or (month == 'march' and 1 <= day <= 19):
#     print('Winter')
# else:
#     print('Invalid Input')

#48
# birthdate = input('Enter the date (month then the day)')
# ind = birthdate.index(' ')
# month = birthdate[:ind]
# day = int(birthdate[ind+1:])
# if (month =='december' and 22 <= day <= 31) or (month == 'january' and 0 <= day <= 19):
#     print('Capricorn')
# elif (month =='january' and 20<= day <= 31) or (month == 'february' and 0 <= day <= 18):
#     print('Aquarius')
# elif (month =='february' and 19<= day <= 29) or (month == 'march' and 0 <= day <= 20):
#     print('Pisces')
# elif (month =='march' and 21<= day <= 31) or (month == 'april' and 0 <= day <= 19):
#     print('Aries')
# elif (month =='april' and 20<= day <= 30) or (month == 'may' and 0 <= day <= 20):
#     print('Taurus')
# elif (month =='may' and 21<= day <= 31) or (month == 'june' and 0 <= day <= 20):
#     print('Gemini')
# elif (month =='june' and 21<= day <= 30) or (month == 'july' and 0 <= day <= 22):
#     print('Cancer')
# elif (month =='july' and 23<= day <= 31) or (month == 'august' and 0 <= day <= 22):
#     print('Leo')
# elif (month =='august' and 23<= day <= 31) or (month == 'september' and 0 <= day <= 22):
#     print('Virgo')
# elif (month =='september' and 23<= day <= 30) or (month == 'october' and 0 <= day <= 22):
#     print('Libra')
# elif (month =='october' and 23<= day <= 31) or (month == 'november' and 0 <= day <= 21):
#     print('Scorpio')
# elif (month =='november' and 22<= day <= 30) or (month == 'december' and 0 <= day <= 21):
#     print('Sagittarius')
# else:
#     print('Invalid input')

#59
# from datetime import datetime
# from calendar import isleap

# date = input("Enter the date (dd.mm.yyyy): ")
# day = int(date[:2])
# print(day)
# month = int(date[3:5])
# print(month)
# year = int(date[6:])
# print(year)
# print(type(month))

# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month ==12 and day == 31:
#     if month == 12:
#         month = 1
#         day = 1
#         year += 1
#     else: 
#         month +=1
#         day = 1
# elif month == 2:
#     if isleap(year):
#         if day == 29:
#             month += 1
#             day = 1
#         else:
#             day += 1
#     else:
#         if day == 28:
#             month += 1
#             day = 1
#         else:
#             day += 1
# else:
#     if day == 30:
#         month += 1
#         day = 1
#     else:
#         day += 1
# print(f"The next day date is: {year}/{month}/{day}")