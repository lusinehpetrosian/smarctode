#72
# for i in range(101):
#     if i % 3 == 0 and i % 5 == 0:
#         print('Fizz-Buzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# 73??????????????????????????????????????????????????????????????????????????????????????????????





# shift = int(input('Enter the shift amount: \n>>'))
# sentence = input('Enter your sentence\n>>')
# for i in range(26-shift):
#     if i in sentence:
#     sentence[i] = sentence[i+shift]
# for i in range(26-shift,26):
#     if i in sentence:
#     sentence[i] = sentence[i-26 + shift]




#75 I think here must be while :/??????????????????????????????????????????????????
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
# print(sentence)
# is_polindrome = True
# for i in range(len(sentence)//2):
#     if sentence[i] != sentence[len(sentence) - i - 1]:
#         is_polindrome = False
#         break
# if is_polindrome == True:
#     print(f'"{oldsentence}" is polindrome!')
# else:
#     print(f'"{oldsentence}" is not polindrome!')

# 77
# print('    ', end = '')
# for i in range (1, 10):
#     print('%4d' % i, end = '')
# print('%4d' % 10)
# for i in range(1, 11):
#     print('%4d' % i, end = '')
#     for j in range(1, 10):
#         print('%4d' % (i*j), end = '')
#     print('%4d' % (10*i))

#67
# perimeter = 0
# first_X =x1 =  int(input('Enter x\n>>'))
# first_Y =y1 = int(input('Enter y\n>>'))

# while True:
#     x2 = input('Enter x\n>>')
#     if x2 == '':
#         break
#     else:
#         x2 = int(x2)
#         y2 = int(input('Enter y\n>>'))
#         perimeter +=(((x1)-(x2))**2 + ((y1)-(y2))**2)**(1/2)
#         x1 = x2
#         y1 = y2
# perimeter += ((first_X-x1)**2 + (first_Y-y1)**2)**(1/2)
# print(perimeter)


#74
# num = int(input('Enter the number\n>>'))
# guess = 1
# while abs(guess**2 - num) > pow(10,-12):
#     guess = (guess + num/guess)/2
# print(guess)










