'''
#123
# text = input('Enter words (only lowercase and separated byspaces:  )')
# text = text.split()
# for i in range(len(text)):    
#     if text[i][-1] in '?!,:':
#         suffix = text[i][-1]
#         text[i]=text[:-1]
#     if text[i][0].isupper():  
#         text[i] = text[i].lower()      
#         if text[i][0] in 'qwrtpsdfghjklzxcvbnm':
#             j = 0
#             while text[i][j] in 'qwrtpsdfghjklzxcvbnm':
#                     j += 1
#             text[i] =text[i][j::]+ text[i][:j]+'ay'
#         elif text[i][0] in 'euoiya':
#             text[i] = text[i]+'way'
#         text[i] = text[i].title()   
#     else:
#         if text[i][0] in 'qwrtpsdfghjklzxcvbnm':
#             j = 0
#             while text[i][j] in 'qwrtpsdfghjklzxcvbnm':
#                     j += 1
#             text[i] =text[i][j::]+ text[i][:j]+'ay'
#         elif text[i][0] in 'euoiya':
#             text[i] = text[i]+'way'
#         # text[i] = text[i].title()
          
# for j in text:
#     print(j, end = ' ')
'''

#124
# xcoords = []
# ycoords = []
# while True:
#     x = input('Enter the coordinate x: ')
#     if str(x) == '':
#         break 
#     xcoords.append(float(x))
#     y = float(input('Enter the coordinate y: '))
#     ycoords.append(y)
# sumx = sum(x for x in xcoords)
# sumy = sum(y for y in ycoords)
# sumxy = 0
# for i in range(len(xcoords)):
#     sumxy += xcoords[i] * ycoords[i]
# sumxp2 = sum(x**2 for x in xcoords)
# m = (sumxy - (sumx * sumy)/len(xcoords))/(sumxp2 - (sumx)**2/len(xcoords))
# b = sumy/len(ycoords) - m * sumx/len(xcoords)
# print(f" y = {'%.2f' % m }x + {'%.2f' % b}")



#126
#125
# print(chr(3))
# from random import randint
# suits = ['s','h','d','c']
# values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
# createddeck =[] 
# for i in suits:
#     for j in values:
#         createddeck.append(j+i)
# print(createddeck)

# for i in range(52):
#     randomindex = randint(0,51)
#     createddeck[i],createddeck[randomindex] = createddeck[randomindex], createddeck[i]
# print(f'Shuffled list is {createddeck}')
# n = int(input('The number of people is : '))
# cardsnum = int(input('The number of cards is : '))
# for i in range(n):
#     for j in range(cardsnum):
#         start = i*j
#         finish = i*j + j
#         cards = createddeck[start:finish]
#     print(f'{i} person gets {cards}')
# _______________________________________________________________
# for i in range(0,n*cardsnum , cardsnum):
#     print(f'PLayer {i//cardsnum + 1} - {createddeck[i: i+ cardsnum]}')
#127
# lst = []
# while True:
#     num = input('Enter a number: ')
#     if num == '':
#         break
#     lst.append(int(num))

# # sorted = True
# asc = True
# desc = True
# for i in range(len(lst)-1):
#     if lst[i]>lst[i+1]:
#         asc = False
#     elif lst[i]<lst[i+1]:
#         desc = False
# if asc == False and desc == False:
#     print('not sorted')
# else:
#     print('sorted')

#128
# import math
# lst1 = []
# while True:
#     num = input('Enter a number: ')
#     if num == '':
#         break
#     lst1.append(int(num))
# lst = []
# for i in lst1:
#     if i not in lst:
#         lst.append(i)
# minimum = float(input('Enter the minimum of the range: '))
# maximum = float(input('Enter the maximum of the range: '))
# newlst = []
# for i in lst:
#     if i>= minimum and i<maximum and i not in newlst:
#         newlst.append(i)
# print(len(newlst))

#133
# nums = []
# sublist =[]
# while True:
#     num = input('Enter a number for sublist: ')
#     if num == '':
#         break
#     sublist.append(int(num))

# while True:
#     num = input('Enter a number: ')
#     if num == '':
#         break
#     nums.append(int(num))
# answer = [[]]
# for i in range(len(nums)):
#     for j in range(len(answer)):
#         if answer[j] == []:
#             answer.append(answer[j] + [nums[i]]) # [] + [1] = [1]
#         elif abs(nums.index(answer[j][-1]) - i) < 2:
#             answer.append(answer[j] + [nums[i]]) # [] + [1] = [1]
# print(sublist in answer)


# Vardges's solution
# nums = []
# while True:
#     num = input('Enter a number: ')
#     if num == '':
#         break
#     nums.append(int(num))
# answer = [[]]
# for i in range(len(nums)):
#     for j in range(len(answer)):
#         answer.append(answer[j] + [nums[i]]) # [] + [1] = [1]
# print(answer)

#134
# nums = []
# while True:
#     num = input('Enter a number: ')
#     if num == '':
#         break
#     nums.append(int(num))
# answer = [[]]
# for i in range(len(nums)):
#     for j in range(len(answer)):
#         if answer[j] == []:
#             answer.append(answer[j] + [nums[i]]) # [] + [1] = [1]
#         elif abs(nums.index(answer[j][-1]) - i) < 2:
#             answer.append(answer[j] + [nums[i]]) # [] + [1] = [1]
# print(sorted(answer, key = len))

#135

# limit = int(input('Enter the range max : ')) 
# lst = list(range(limit + 1))
# lst[1] = 0
# p = 2
# while p < limit:
#     for i in range(p * 2, limit+1, p):
#         lst[i] = 0  
#     p += 1
# prime_numbers = []
# for i in lst:
#     if i != 0:
#         prime_numbers.append(i)
# print(prime_numbers)

# list input variant 
# smaller = eval(input('Enter list   '))
# print(smaller)