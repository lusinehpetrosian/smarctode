#66
# totalcost = 0
# while True:
#     prices = input('Enter the prices for item\n>>>')
#     if prices == '':
#         break
#     else:
#         prices = float(prices)
#         notcash = totalcost = totalcost + prices
#     if totalcost % 5 < 2.5:
#         totalcost = totalcost - totalcost % 5
#     else: 
#         totalcost = totalcost + 5 - totalcost % 5
# print(f'Total cost with cents is {notcash}')
# print(f'In cash you have to pay {totalcost}')

#68
# s = 0
# k = 0
# while True:
#     letter = input('Enter the grade: ')
#     if letter == '':
#         break
#     elif letter == 'A+':s += 4
#     elif letter == 'A':s += 4
#     elif letter =='A-':s += 3.7
#     elif letter =='B+':s += 3.3
#     elif letter =='B':s += 3.0
#     elif letter =='B-':s += 2.7
#     elif letter =='C+':s += 2.3
#     elif letter =='C':s += 2.0
#     elif letter =='C-':s += 1.7
#     elif letter =='D+':s += 1.3
#     elif letter =='D':s += 1.0
#     elif letter =='F':s += 0
#     k += 1
# print('GPA is', round((s/k), 2))
    
#69
# totalcost = 0
# while True:
#     age = input('Enter the age of atendee: ')
#     if age == '':
#         break
#     age = int(age)
#     if 3 <= age <= 12:
#         totalcost += 14
#     elif 13 <= age <= 65:
#         totalcost += 23
#     elif age > 65:
#         totalcost += 18
# print('This group has to pay', '%.2f' % totalcost,'$ to enter the zoo')
    
#70 ????? should I notice that in bits must be only 0 or 1???????
# while True:
#     bits = input('Enter 8 bits(0 or 1): ')
#     if bits == '':
#         break
#     else:
#         if len(bits) != 8 or bits.replace('0', '').replace('1','')!='':
#             print('Error, You have to insert 8 bits which contin only 0 and 1!!!!!!')
#         else:
#             numberof1 = bits.count('1')
#             if numberof1 % 2 == 1:
#                 print('Parity bit is 1') 
#             else:
#                 print('Parity bit is 0') 

#75
# word = input('Enter your word\n>> ')
# is_polindrome = True
# for i in range(len(word)//2):
#     if word[i] != word[len(word) - i - 1]:
#         is_polindrome = False
#         break
# if is_polindrome == True:
#     print(f'{word} is polindrome!')
# else:
#     print(f'{word} is not polindrome!')

#76
# sentence = input('Enter your sentence\n>> ')
# oldsentence = sentence
# sentence = sentence.replace(' ','')
# sentence = sentence.replace(',','')
# sentence = sentence.lower()
# is_polindrome = True
# for i in range(len(sentence)//2):
#     if sentence[i] != sentence[len(sentence) - i - 1]:
#         is_polindrome = False
#         break
# if is_polindrome == True:
#     print(f'"{oldsentence}" is polindrome!')
# else:
#     print(f'"{oldsentence}" is not polindrome!')

#80
# num = 72
# factor = 2
# while num >= factor:
#     if num % factor == 0:
#         print(factor)
#         num //= factor
#     else:
#         factor += 1







#81
# binary = input('Enter the binary number: ')
# decimal = 0 
# for i in binary:
#     decimal = int(i) + decimal * 2
# print(decimal)
'''
n = 1
while True:
    print(n)
    n += 1
'''
#82
# result = ''
# q = int(input('The number to convert is:  '))
# while q > 0:
#     r = q % 2
#     r = str(r)
#     result = r + result
#     q = q//2
# print(result,'is binary!')
#2nd type of solution)))))))))
# print(bin(q)[2:])





