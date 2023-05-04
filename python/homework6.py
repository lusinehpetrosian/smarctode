#41
# a = int(input('Enter first side: '))
# b = int(input('Enter second side: '))
# c = int(input('Enter third side: '))
# if a>0 and b>0 and c>0:
#     if a + b > c and a + c > b and b + c >0:
#         if a == b == c:
#             print('The triangle is equilateral!')
#         elif a == b != c or a == c != b or a != b == c:
#             print('The triangle is isosceles!')
#         else:
#             print('The triangle is scalene!')
#     else:
#         print('Invalid input!')
# else:
#     print('Invalid input!')

#42

# # 42
# C4 = 261.63
# D4 = 293.66
# E4 = 329.63
# F4 = 349.23
# G4 = 392.00
# A4 = 440.00
# B4 = 493.88
# note = input('Enter note: ')
# octave = int(input('Enter octave(0-8): '))

# if note == 'A':
#     print(A4 / pow(2 , 4 - octave))
# elif note == 'B':
#     print(B4 / pow(2 , 4 - octave))
# elif note == 'C':
#     print(C4 / pow(2 , 4 - octave))
# elif note == 'D':
#     print(D4 / pow(2 , 4 - octave))
# elif note == 'E':
#     print(E4 / pow(2 , 4 - octave))
# elif note == 'F':
#     print(F4 / pow(2 , 4 - octave))
# elif note == 'G':
#     print(G4 / pow(2 , 4 - octave))

#43
# C4 = 261.63
# D4 = 293.66
# E4 = 329.63
# F4 = 349.23
# G4 = 392.00
# A4 = 440.00
# B4 = 493.88
# frequency = float(input('The frequency of note is : : '))
# if C4 - 1 < frequency < C4 + 1:
#     print('Note is C4')
# elif D4 - 1 < frequency < D4 + 1:
#     print('Note is D4')    
# elif E4 - 1 < frequency < E4 + 1:
#     print('Note is E4')
# elif F4 - 1 < frequency < F4 + 1:
#     print('Note is F4')
# elif G4 - 1 < frequency < G4 + 1:
#     print('Note is G4')
# elif A4 - 1 < frequency < A4 + 1:
#     print('Note is A4')
# elif B4 - 1 < frequency < B4 + 1:
#     print('Note is B4')
# else:
#     print('The frequency does not correspond to a known note!!!!')

#44
# amount = int(input('Enter the amount ::'))
# if amount == 1:
#     print('George Washington')
# elif amount == 2:
#     print('Thomas Jefferson')
# elif amount == 5:
#     print('Abraham Lincoln')
# elif amount == 10:
#     print('Alexander Hamilton')
# elif amount == 20:
#     print('Andrew Jackson ')
# elif amount == 50:
#     print('Ulysses S. Grant')
# elif amount == 100:
#     print('Benjamin Franklin')
# else:
#    print('Error, Invalid Input!')

#45 

# month = input('Month? :')
# day = int(input('Day? :'))
# if month == 'january' and day == 1:
#     print("New Year's Day")
# elif month == 'july' and day == 1:
#     print('Canada Day')
# elif month == 'december' and day == 25:
#     print('Christmas Day')
# else:
#     print('There is no holiday this day!!')

#46
# l = input('letter is : ')
# d = int(input('digit is : '))
# if l == 'a' or l == 'c' or l == 'e' or l == 'g':
#     if d%2==1:
#         print('black')
#     else:
#         print('white')
# elif l == 'b' or l == 'd' or l == 'f' or l == 'h':
#     if d%2==0:
#         print('black')
#     else:
#         print('white')  

#47
'''
# month = input('Month? :')
# day = int(input('Day? :'))
# if (0 <= day <= 31 and (month =='march' or month == 'may')) or (0 <= day <= 30 and month =='april'):
#     print('Spring')
# elif (0 <= day <= 31 and (month =='july' or month == 'august')) or (0 <=day <= 30 and month =='june'):
#     print('Summer')
# elif (0 <= day <= 30 and (month =='september' or month == 'november')) or (0 <=day <= 31 and month =='october'):
#     print('Autumn')
# elif (0 <= day <= 31 and (month =='december' or month == 'january')) or (0 <=day <= 29 and month =='february'):
#     print('Winter')
# else:
#     print('Invalid Input')
'''
#48
# month = input('Month? :')
# day = int(input('Day? :'))
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

# #49
# year = int(input('YEAR? :::: '))
# if year >=0:
#     if year %12 == 0:
#         print('Monkey')
#     elif year %12 == 1:
#         print('Rooster')
#     elif year %12 == 2:
#         print('Dog')
#     elif year %12 == 3:
#         print('Pig')
#     elif year %12 == 4:
#         print('Ratt')
#     elif year %12 == 5:
#         print('Ox')
#     elif year %12 == 6:
#         print('Tiger')
#     elif year %12 == 7:
#         print('Hare')
#     elif year %12 == 8:
#         print('Dragon')
#     elif year %12 == 9:
#         print('Snake')
#     elif year %12 == 10:
#         print('Horse')
#     elif year %12 == 11:
#         print('Sheep')

#50

# magnitute = float(input('Enter the magnitute'))
# if 0 <= magnitute < 2:
#     print('Micro')
# elif 2 <= magnitute < 3:
#     print('Very minor')
# elif 3 <= magnitute < 4:
#     print('Minor')
# elif 4 <= magnitute < 5:
#     print('Light')
# elif 5 <= magnitute < 6:
#     print('Moderate')
# elif 6 <= magnitute < 7:
#     print('Strong')
# elif 7 <= magnitute < 8:
#     print('Major')
# elif 8 <= magnitute < 10:
#     print('Great')
# elif  magnitute >= 10:
#     print('Meteoric')
# else:
#     print('Invalid input')


