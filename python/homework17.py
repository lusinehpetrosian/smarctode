#104
# def hex2int(n):
#     lst = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
#     n = n.upper()
#     if n not in lst:
#         print('Invalid input!!')
#     elif n in lst:
#         return lst.index(n)
# print(hex2int('a'))
# def int2hex(n):
#     lst = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
#     if n<0 or n>=16:
#         return 'Invalid input!!'
#     else:
#         return lst[n]
# print(int2hex(7))

#105
# def from_x_to_y(num, start_base, end_base):
#     num = str(num)
#     if start_base < 2 or start_base > 16 or end_base < 2 or end_base > 16:
#         return 'Error'
#     digits = {0: '0',
#               1: '1',
#               2: '2',
#               3: '3',
#               4: '4',
#               5: '5',
#               6: '6',
#               7: '7',
#               8: '8',
#               9: '9',
#               'A': 'A',
#               'B': 'B',
#               'C': 'C',
#               'D': 'D',
#               'E': 'E',
#               'F': 'F',
#              }
#     num_10 = int(num, base = start_base)
#     if end_base == 10:
#         return num_10
#     result = ''
#     while num_10 != 0:
#         d = num_10 % end_base
#         result = digits[d] + result
#         num_10 = num_10 // end_base
#     return result
# print(from_x_to_y('27', 10, 2))


#106
# from calendar import isleap
# def daysinmonth(year, month):
#     lst = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if isleap(year) and month == 2:
#         return lst[month-1]+1
#     else:
#         return lst[month-1]

# year = int(input('Year is : '))
# month = int(input('month is : '))
# print(daysinmonth(year, month))

#107
# from math import gcd
# def fraction(a,b):
#     return f'{a//gcd(a,b)}/{b//gcd(a,b)}'
# a = int(input('Enter the numerator : ')) 
# b = int(input('Enter the denominator : ')) 
# print(fraction(a,b))

#108
# def measure(numbers, unit):
#     if unit =='teaspoon':
#         teaspoon = numbers
#     elif unit == 'tablespoon':
#         teaspoon = numbers * 3
#     elif unit == 'cup':
#         teaspoon = numbers * 3 * 16
#     numofcups = teaspoon//48
#     teaspoon = teaspoon - numofcups * 48
#     numoftablespoons = teaspoon//3
#     teaspoon = teaspoon - numoftablespoons * 3
#     numofteaspoons = teaspoon
#     answer = ''
#     if numofcups == 1:
#         answer = answer + '1 cup'
#     elif numofcups > 1 :
#         answer = answer + str(numofcups) + ' cups'
#     if numoftablespoons == 1:
#         answer = answer + '1 tablespoon'
#     elif numoftablespoons > 1:
#         answer = answer +' '+ str(numoftablespoons) + ' tablespoons'
#     if numofteaspoons == 1:
#         answer = answer + '1 teaspoon'
#     elif numofteaspoons > 1:
#         answer = answer + ' ' +str(numofteaspoons) +' teaspoons'
#     return answer
# numbers = int(input('Enter the number of units: '))
# unit = input('Enter the unit : ')
# print(measure(numbers, unit))



#109
# def magicdate(day,month,year):
#     return day * month == year %100
# for year in range(1900,2001):
#     for month in range(1, 13):
#         for day in range(1,daysinmonth(year,month)+1):

#             if magicdate(day, month, year):
#                 print("%02d/%02d/%04d." % (day,month,year))


# def generate(numRows):
#     lst = []
#     for i in range(1,numRows +1):
#         lst.append(i * [1])
#     for i in range(2, numRows):
#         for j in range(1, len(lst[i])-1):
#             lst[i][j] = lst[i-1][j-1] + lst[i-1][j]
#     return lst
# print(generate(5))
