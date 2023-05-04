#91
# from calendar import isleap
# def ordinal(day,month, year):
#     num = 0
#     lst = [31,28,31,30,31,30,31,31,30,31,30,31]
#     if isleap(year) and month>2:
#         for i  in range(month-1):
#             num = num + lst[i]
#         num += day+1 
#         return num
#     else:
#         for i  in range(month-1):
#             num = num + lst[i] 
#         num+= day
#         return num
# print(ordinal(8,4,2023))


#93
# def f(s,w):
#     if len(s) >= w:
#         return s
#     else:
#         return (abs((len(s) - w)) // 2 * ' ' + s)
# s = input('Enter your string: ')
# w = int(input('Enter the length of window: '))
# print(f(s,w))

#98
# def prime(n):
#     isornot = True
#     for i in range(2,n//2+1):
#         if n % i == 0:
#             isornot = False
#     return isornot
# print(prime(4))

# def isprime(num):
#     for i in range(2,num):
#         if num & i == 0:
#             return False
#         return True



#99
# def prime(n):
#     isornot = True
#     for i in range(2,n//2+1):
#         if n % i == 0:
#             isornot = False
#     return isornot
# print(prime(4))
# n = int(input('Enter your number: '))
# def nextprime(n):
#     n += 1
#     while True:
#         if prime(n):
#             return n
#         else:
#             n = n+1
# print(nextprime(n))

#100
# from random import choice, randint
# def password():
#     s = ''
#     for i in range(randint(7,11)):
#         s += chr(choice(range(33,127)))
#     return s
# print(password())

    
