
# 51
# from math import sqrt
# a = int(input('Enter a: '))
# b = int(input('Enter b: '))
# c = int(input('Enter c: '))

# D = b**2 - 4 * a * c
# if a != 0:
#     if D > 0:
#         x1 = (-b + sqrt(D)) / (2 * a)
#         x2 = (-b - sqrt(D)) / (2 * a)
#         print(f'first root is {round(x1 , 2)}, second root is {round(x2 , 2)}')
#     elif D == 0:
#         x = (-b) / (2 * a)
#         print(f'The root is {round(x , 2)}')
#     else:
#         print('No roots')
# else:
#     print('a cant be 0')

#52
# letter = input('letter grade is : ')

# if letter == 'A+' or letter == 'A':
#     print(4.0)
# elif letter =='A-' :
#     print(3.7)
# elif letter =='B+' :
#     print(3.3)
# elif letter =='B' :
#     print(3.0)
# elif letter =='B-' :
#     print(2.7)
# elif letter =='C+' :
#     print(2.3)
# elif letter =='C' :
#     print(2.0)
# elif letter =='C-' :
#     print(1.7)
# elif letter =='D+': 
#     print(1.3)
# elif letter =='D':
#     print(1.0)
# elif letter =='F':
#     print(0)
# else:
#     print('Invalid input!')

#53
# grade =float(input(' grade is : '))
# if grade >= 3.9:
#     print('A+')
# elif 3.5<=grade <3.9:
#     print('A-')
# elif 3.2<=grade<3.5 :
#     print('B+')
# elif 2.9<=grade<3.2 :
#     print('B')
# elif 2.5<=grade<2.9 :
#     print('B-')
# elif 2.2<=grade<2.5 :
#     print('C+')
# elif 1.9<=grade<2.2:
#     print('C')
# elif 1.5<=grade<1.9:
#     print('C-')
# elif 1.2<=grade<1.5: 
#     print('D+')
# elif 0.5<=grade<1.2:
#     print('D')
# elif 0<=grade<0.5:
#     print('F')
# else:
#     print('Invalid input!')

#54
# rate = float(input('The rate of an employee is : '))
# if rate == 0.0:
#     print(f'Unacceptable Performance and the raise is {rate*2400}$')
# elif rate == 0.4:
#     print(f'Acceptable Performance and the raise {rate*2400} is $')
# elif rate >= 0.6:
#     print(f'Meritorious Performance and the raise is {rate*2400}$')
# else: 
#     print('Invalid input!')

#55
# length = int(input('The length of wave is : '))
# if length < 380 or length > 750:
#     print( 'The wavelength entered by the user is outside of the visible spectrum')
# elif 380 <= length <= 450:
#     print('Violet')
# elif 450 <= length <= 495:
#     print('Blue')
# elif 495 <= length <= 570:
#     print('Green')
# elif 570 <= length <= 590:
#     print('Yellow')
# elif 590 <= length <= 620:
#     print('Orange')
# elif 620 <= length <= 750:
#     print('Red')

#56
# frange = float(input("Frequency range(Hz)"))
# if frange <= 3*10**9:
#     print('Radie Waves')
# elif 3*10**9<= frange <=3*10**12:
#     print('Microwaves')
# elif 3*10**12 <= frange  <= 4.3*10**14:
#     print('Infrared Light')
# elif 4.3*10**14 <= frange  <= 7.5*10**14:
#     print('Visible Light')
# elif 7.5*10**14 <= frange <= 3*10**17:
#     print('Ultraviolet light')
# elif 3*10**17 <= frange <= 3*10**19:
#     print('X- rays')
# elif 3*10**19 <= frange:
#     print('gamma rays')

#57
# minutes = int(input('Enter count of minutes: '))
# sms = int(input('Enter count of sms: '))
# money = 15

# if minutes <= 50 and sms <= 50:
#     pass
# elif minutes > 50 and sms <= 50:
#     money += (minutes - 50) * 0.25
# elif minutes <= 50 and sms > 50:
#     money += (sms - 50) * 0.15
# elif minutes > 50 and sms > 50:
#     money += (sms - 50) * 0.15 + (minutes - 50) * 0.25

# money = (money + 0.44) * 1.05
# print(f"You need to pay $ {round(money , 2)}")

#58
# from calendar import isleap
# year = int(input('Year is : '))
# print(isleap(year))

# year = int(input('Year is : '))
# if year >= 0:
#     if year % 400 == 0:
#         print(True)
#     elif year %100 == 0:
#         print(False)
#     elif year%4 == 0:
#         print(True)
#     else:
#         print(False)
# else:
#     print("Invalid input!")

#59
# import datetime

# year = int(input('Enter year: '))
# month = int(input('Enter month: '))
# day = int(input('Enter day: '))
# date = datetime.datetime(year , month, day)
# print(f'your date is {date}')
# days = int(input('Enter count of days: '))
# after = date + datetime.timedelta(days=days)
# print(f'After {days} days will be {after}')

# 2nd variance
# from datetime import datetime
# from calendar import isleap

# date = input("Enter the date (dd.mm.yyyy): ")

# date_int = datetime.strptime(date, "%d.%m.%Y")
# day = date_int.day
# month = date_int.month
# year = date_int.year
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

#60
# from math import floor
# year = int(input('Year is : '))
# day_of_week = (year + floor((year - 1)/4) - floor((year - 1)/100) + floor((year - 1)/400))%7
# if day_of_week == 0:
#     print('Sunday')
# elif day_of_week == 1:
#     print('Monday')
# elif day_of_week == 2:
#     print('Tuesday')
# elif day_of_week == 3:
#     print('Wednesday')
# elif day_of_week == 4:
#     print('Thursday')
# elif day_of_week == 5:
#     print('Friday')
# elif day_of_week == 6:
#     print('Saturday')

#61
'''
letters = input('Enter the letters  :  ')
digits = input('Enter the number')
#?????????????????????????????????????????????????????????????????????
if 0<int(digits)<9999:
    if len(letters) != 3 and letters.upper() != True:
        print('Invalid input')
    else:
        if len(digits)==3:
            print('Older style license plate')
        elif len(digits)==4:
            print('Newer style license plate')
        else:
            print('Invaliid input!')
else: 
    print('Invalid input!')
'''
# #62
# from random import choice
# red = 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36
# black = 2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35
# zeros = '00' , '0'
# randomnum = choice(zeros + red + black)
# print('Winning number', randomnum)
# if randomnum == '0' or randomnum == '00':
#     print(f'Won {randomnum}')
# else:
#     if randomnum in red:
#         print(f'{randomnum} is red!')
#     elif randomnum in black:
#         print(f'{randomnum} is black')
#     if randomnum % 2 == 0:
#         print(f'{randomnum} is even')
#     else:
#         print(f'{randomnum} is odd')
#     if 1<= randomnum <= 18:
#         print(f'{randomnum} in 1 to 18')
#     else:
#         print(f'{randomnum} in 19 to 36')






