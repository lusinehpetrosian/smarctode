#1
# print('Lusine Petrosyan')
# print('3309')
#2
# name = input('What is your name???')
# print('Hello,', name)
#3
# length = float(input('Enter the kength of the room: '))
# width  = float(input('Enter the width of the room: '))
# print('S = ', length * width, 'metres')
#4 1akr=  43 560ft^2
# length = float(input('Enter the kength of the yardin ft: '))
# width  = float(input('Enter the width of the yard in ft: '))
# print('S = ', length * width / 43560, 'akr')
#5
# num1 = float(input('The number of bottles <=1 litres: '))
# num2 = float(input('The number of bottles >1 litres: '))
# print('You gained $',num1 * 0.10 + num2 * 0.25)
#6
# payment = float(input('Enter the cost, please! '))
# tax = payment*0.2
# tip = payment*0.18
# print (f'tax = {tax}\ntip = {tip}\n')
# print('The tax from your payment is', payment*0.2)
# print('The tip from your payment is', payment*0.18)
# print('You have to pay: ', payment + payment * 0.38 )

#7
# n = int(input('Enter yor integer number:'))
# print('S = ', n*(n+1)/2)
#8
# a = int(input('Enter the number of the trinkets: '))
# b = int(input('Enter the number of the suvenirs: '))
# c = float(input('Enter the weight of other things: '))
# print('The whole weight is', a * 112 + b * 75 + c)
#9
# money = float(input('The amount of money'))
# print(round(money * (1.04), 2))
# print(round(money * (1.04)**2, 2))
# print(round(money * (1.04)**3, 2))
#10
# import math
# a = int(input('The first digit: '))
# b = int(input('The second digit: '))
# print(a + b)
# print(abs(a - b))
# print(a * b)
# print(a//b)
# print(a % b)
# print(math.log10(a))
# print(a ** b)
#11
# USA = float(input('Enter the needed amount in US milles-per-gallon: '))
# print('Kanadian is:', 0.425 * USA )
#12
# from math import sin, cos, radians
# from math import acos as arccos
# t1 = radians(float(input('Enter the first coordinate in degrees')))
# g1 = radians(float(input('Enter the second coordinate in degrees')))
# t2 = radians(float(input('Enter the first coordinate in degrees')))
# g2 = radians(float(input('Enter the second coordinate in degrees')))
# print( 'Distance = ',6371.01 * arccos(sin(t1)*sin(t2)+ cos(t1)*cos(t2)*cos(g1-g2)))
#13
"""
change = int (input('Enter change: '))
toonies = change // 200
change = change % 200
loonies = change // 100
change = change % 100
cent_25 = change // 25
change = change % 25
cent_10 = change // 10
change = change % 10
cent_5 = change // 5
change = change % 5
cent_1 = change
print(f'''
toonies = {toonies}
loonies = {loonies}
cent_25 = {cent_25}
cent_10 = {cent_10}
cent_5 = {cent_5}
cent_1 = {cent_1}
''')
"""
# a = float(input('The change in cents is:  '))
# n25 = a // 25
# print('Needed number of 25 is', n25)
# n10 = (a - n25 * 25) // 10
# print('Needed number of 10 is', n10)
# n5 = (a - n25 * 25 - n10 * 10) // 5
# print('Needed number of 5 is', n5)
# n1 = (a - n25 * 25 - n10 * 10 - n5 * 5) // 1
# print('Needed number of 1 is', n1)

#14 1 ft = 30,48sm, 1dy = 2,54sm
# a = float(input('Enter your height in ft: '))
# b = float(input('Enter your height in duym: '))
# print('In sm your height is ', a * 30.42 + b * 2.54)
#15
# 1ft= 0,333333yard = 11,999988duym =0,00018939375 mil
# a = float(input('The distance in ft is:  '))
# ad = a // 12
# print(ad,'duym')
# ay = (a - ad * 12) // 0.3
# print(ay, 'yard')
# am = (a - ad * 12  - ay * 0.3) // 0.0001894
# print(am, ',mil')
#16
# from math import pi 
# r = float(input('Enter the radius: '))
# print('S = ', pi * r**2)
# print('V = ', 4/3*pi*r**3)
#17   q = mCDT.
# m = float(input('How muvh water do we need?  '))
# t = float(input('How many degrees do we have to change the temerature?  '))
# print ('We need', m * t * 4.186,'Joul')
# print('We need ', m * t * 4.186/3600000, 'kWh')
#18
# from math import pi
# h = float(input('The height is: '))
# r = float(input('The radius is: '))
# print('V = ',pi * r ** 2 * h)

#19
# from math import sqrt
# h = float(input('Height in metres: '))
# print ('V = ', sqrt(9.8*2*h))
#20
# p = float(input('Enter the pressure: '))
# v = float(input('Enter the volume: '))
# T = float(input('Enter the temperaure in Celsius: '))+273.15
# print("n = ", p*v/(T*8.314))




