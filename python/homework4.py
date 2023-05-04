#21
# b = float(input('Enter the length of the base: '))
# h = float(input('Enter the height: '))
# s = b * h / 2
# print('S = ', s)

#22
# s1 = float(input('S1 = '))
# s2 = float(input('S2 = '))
# s3 = float(input('S3 = '))
# p = (s1 + s2 + s3)/2
# from math import sqrt
# S = sqrt(p* (p-s1)*(p-s2)*(p-s3))
# print(f'S ={S}')

#23
# from math import tan, pi
# s = float(input('The length: '))
# n = int(input('The number of angles: '))
# area = n * s**2/(4 * tan(pi/n))
# print(f'area = {round(area,4)}')
 
#24
# import datetime
# seconds = int(input('Seconds: '))
# minutes = int(input('Minutes: '))
# hours = int(input('Hours: '))
# days = int(input('Days: '))
# print ('Secs =', seconds + minutes*60 + hours * 3600 +days *24*3600)

#25
# import datetime
# now = datetime.datetime.now()
# print(f'now {now}')
# seconds = int(input('seconds = '))
# after = now +datetime.timedelta(seconds=seconds)
# print(f' after {after}')

#26
# import time
# print(time.asctime())

#27
# import math
# year = int(input('Enter the year: '))
# a = year % 19
# b = year // 100
# c = year % 100
# d = b//4
# e = b % 4
# f = (b+8)//25
# g = (b-f+1)//3
# h = (19*a +b - d - g +15) % 30
# i = c // 4
# k = c % 4
# l =(32 + 2*e + 2*i - h - k) % 7
# m = (a + 11*h + 22*l)//451
# month = (h + l + 7*m + 114) // 31
# day = 1 + (h + l - 7*m + 114) % 31
# print(f'{day}/{month}/{year}')

# 28 ________________________???????????????____________________________
# weight = int(input('Weight = '))
# height = int(input('Height = '))
# print('BMI =', weight/height**2)

#29 WCI = 13,12 + 0,6215Ta - 11,37V0,16 + 0,3965TaV0,16.
# t = float(input('Temperature = '))
# v = float(input('Speed = '))
# print(f'WCI = {13.12 + 0.6215 * t - 11.37 * v**(4/25) + 0.3965 * t * v**(4/25) }')

#30
# t = float(input('temperature(C) = '))
# print(f'Temperature (K) = {t + 273.15}\nTemperature (F) = {t * 9/5 + 32}')

#31
# p = float(input('Pressure (kpa) = '))
# print(f'Pressure (f/d^2) = {p/6895}\nPressure (PSI) = {p * 7501}')

#32 ________
# num = int(input('Number = '))
# sum = 0
# while num:
#     a = num % 10
#     num = num // 10
#     sum += a
# print(sum)


# ______
# num = input('Number = ')
# print(f'sum = {int(num[0])+int(num[1])+ int(num[2])+ int(num[3])}')

#33
# int1 = int(input('Int1 = '))
# int2 = int(input('Int2 = '))
# int3 = int(input('Int3 = '))
# minimum = min(int1, int2, int3)
# maximum = max(int1, int2, int3)
# print(minimum, int1 + int2 +int3 - minimum - maximum, maximum)

#34
# n = int(input("Number of yesterday's bread = "))
# p = 3.49
# print(f'The real price is {p} $\nThe discounted price is {round(p*0.4,2)}\nYesterday income is {round(p*0.4*n,2)}')
     







