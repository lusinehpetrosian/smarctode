#111
# mylist = []
# while True:
#     n = int(input('Enter the nums: '))
#     if n == 0:
#         break
#     else:
#         mylist.append(n)
# print(sorted(mylist)[::-1])


#112
# mylist = []
# while True:
#     n = int(input('Enter the nums: '))
#     if n == 0:
#         break
#     else:
#         mylist.append(n)
# mylist.remove(min(mylist))
# mylist.remove(max(mylist))
# print(mylist)


#114
# zeros = []
# minuses = []
# pluses = []
# while True:
#     n = input('Enter a number: ')
#     if n == '':
#         break
#     elif int(n) == 0:
#         zeros.append(n)
#     elif int(n) > 0:
#         pluses.append(n)
#     elif int(n) < 0:
#         minuses.append(n)
# print(minuses + zeros + pluses)

'''#116 ______________haven't used a list_____________________________'''
# for n in range(1,10001):
#     sum = 0
#     for i in range(1,n):
#         if n % i == 0:
#             sum += i
#             if sum == n:
#                 print(n)

#117
# text = "Contractions include: don't, isn't, and wouldn't."
# syms = list('!@#$%^&*()_+:,<>?[]{}.')
# for i in syms:
#     text = text.replace(i,'')
# text  = text.split()
# print(text)

#118

# text = input('Enter your sentence: ')
# text = text.lower()
# syms = list('!@#$%^&*()_+:,<>?[]{}.')
# for i in syms:
#     text = text.replace(i,'')
# text = text.split()
# print('Polindrome' if text == text [::-1] else 'Not polindrome')

#119
# mylist = []
# sum = 0
# count = 0
# while True:
#     n = int(input('Enter the nums: '))
#     if n == 0:
#         break
#     else:
#         mylist.append(n)
#         sum += n 
#         count += 1
# mylist.sort()
# ________________________________________________________________________________________
# av = sum/count
# print('Average is', av )
# below = []
# above = []
# equal = []
# for i in mylist:
#     if i < av:
#         below.append(i)
#     elif i > av:
#         above.append(i)
#     else:
#         equal.append(i)
# print(f'Below average are{below}\nEqual average are{equal}\nAbove average are{above}')
# ___________________________________________________________________________________________
# mean = sum(mylist)/len(mylist)
'''We can also do count mean like this'''

#120
# lst = []
# while True:
#     word = input('Enter a word: ')
#     if word == '':
#         break
#     else:
#         lst.append(word)
# if len(lst)== 1:
#     print(lst[0])
# elif len(lst)== 2:
#     print(f'{lst[0]} and {lst[-1]}')
# else:    
#     '''
#     print(' , '.join(mylist[:-1]) +f' and {mylist[-1]} )
#     '''  
#     for i in range(len(lst)-1):
#         print(lst[i], end =', ')
#     print('and', lst[-1] )

#121
# from random import randint
# nums = []
# while len(nums)!=6:
#     numinticket = randint(1,49)
#     if numinticket not in nums:
#         nums.append(numinticket)     
# print(sorted(nums))     
# __________________________________________________________________________________
# import random
# mylist= [i for i in range(1,50)]
# random.shuffle(mylist)
# ticket = mylist[:6]
# print(ticket)

#122
#______________________________________________________we can also write for i in text Lus jaaaaaaaaaan
# text = input('Enter words (only lowercase and separated byspaces:  )')
# text = text.split()
# for i in range(len(text)):
#     if text[i][0] in 'qwrtpsdfghjklzxcvbnm':
#         j = 0
#         while text[i][j] in 'qwrtpsdfghjklzxcvbnm':
#                 j += 1
#         text[i] =text[i][j::]+ text[i][:j]+'ay'
#     elif text[i][0] in 'euoiya':
#         text[i] = text[i]+'way'
# for j in text:
#     print(j, end = ' ')





