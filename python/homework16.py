#92
# import datetime
# def OrdinalDate(year , month , day):
#     start_year = datetime.datetime(year , 1 , 1)
#     input_date = datetime.datetime(year , month , day)
#     return (input_date - start_year).days + 1
# print(OrdinalDate(2023 , 4 , 8))


# import datetime
# def GregorianDate(year,day):
#     start_year = datetime.datetime(year , 1 , 1)
#     return start_year + datetime.timedelta(days = day-1) 
# print(GregorianDate(2023, 98))

# year = int(input('Enter the year: '))
# ordinalday = int(input('Enter the ordinal day: '))
# print(GregorianDate(year, ordinalday + 280))

#94
# def triangle(a,b,c):
#     return a+b>c and b+c>a and a+c>b
# a = int(input('Enter the first length: '))
# b = int(input('Enter the second length: '))
# c = int(input('Enter the third length: '))
# print(triangle(a,b,c))

#95
# def capitalise(text):
#     new = ''
#     char = ''
#     for i in range(len(text)):
#         if i == 0 or char in ['.', '?', '!', '. ', '? ', '! ']:
#             new += text[i].upper()
#         elif text[i] == 'i' and char[1] == ' ' and text[i+1] in "' .?!":
#             new += 'I'
#         else:
#             new += text[i]
#         char = text[i-1] + text[i]
#     return new
# text = input('Enter your text: ')
# print(capitalise(text))

#96
# def isinteger(text):
#     text = text.strip()
#     if text.isdigit():
#         return True
#     elif (text[0]=='+' and text[1:].isdigit()) or (text[0]=='-' and text[1:].isdigit()):
#         return True
#     else:
#         return False
# text = input('Enter your string: ')
# print(isinteger(text))

#97
# def precedence(text):
#     if text in ['+','-']:
#         return 1
#     elif text in ['*', '/']:
#         return 2
#     elif text == '^':
#         return 3
#     else:
#         return -1
# text = input('Enter an operator: ')
# if precedence(text) == -1:
#     print('Invalid input')
# else:
#     print('It is operator')

#100
# from random import choice, randint
# def password():
#     s = ''
#     for i in range(randint(7,11)):
#         s += chr(choice(range(33,127)))
#     return s
# print(password())

#101 

# from random import choice, randint
# def password():
#     s = ''
#     length = randint(6,8)
#     if length == 6:
#         for i in range(3):
#             s += chr(choice(range(65,91)))
#         for i in range(3):
#             s += chr(choice(range(48,58)))
#     else:
#         for i in range(4):
#             s += chr(choice(range(48,58)))
#         for i in range(3):
#             s += chr(choice(range(65,91)))
#     return s
# print(password())

#102
# def passwordissafe(s):
#     uppers = False
#     lowers = False
#     digits = False
#     if len(s)<8:
#         return False
#     else:
#         for i in s:
#             if 65<=ord(i)<=90:
#                 uppers = True
#                 break
#             elif 97<=ord(i)<=122:
#                 lowers = True
#             elif 48<=ord(i)<=57:
#                 digits = True
#     if uppers == True and lowers == True and digits == True:
#         return True
#     else:
#         return False
# password = input('Enter your pass: ')
# print(passwordissafe(password))

#102 in a normal way 
# def passwordissafe(s):
#     uppers = False
#     lowers = False
#     digits = False
#     if len(s)< 8:
#         return False
#     for i in s:
#         if i.isdigit():
#             digits = True
#         if i.isupper():
#             uppers = True
#         if i.islower():
#             lowers = True
#     return digits and uppers and lowers

#103
# def randomvalidpass():
#     passwordattempt = password()
#     k = 1
#     while passwordissafe(passwordattempt) == False:
#         passwordattempt = password()
#         k += 1
#     return passwordattempt, k
# print(randomvalidpass())


