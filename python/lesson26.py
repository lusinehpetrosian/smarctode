# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     else:
#         return factorial(n-1) * n
# n = int(input('Enter the num : '))
# print(factorial(n))

# def fib(n):
#     if n == 1 or n == 2:
#         return n -1
#     else:
#         return fib(n-1) + fib(n-2)
# n = int(input('Enter the num : '))
# print(fib(n))

# def fib(n):
#     a,b = 0,1
#     for i in range(n-1):
#         a , b = b, a + b
#     return (a)
# n = int(input('Enter the num : '))
# print(fib(n))

# 1
# hello -> H*e*l*l*o
# def inputsym(s):
#     if len(s) == 1:
#         return s
#     return s[0] + '*' + inputsym(s[1:])
# print(inputsym('Hello'))

# 2
# def brackets(s):
#     if len(s) == 1 or len(s) == 2:
#         return s
#     else:
#         return s[0] + '(' + brackets(s[1:len(s)-1]) + ')' + s[-1]
# s = input('Enter the text: ')
# print(brackets(s))


#173
# def summ(sumofnums = 0):
#     num = input('Enter the needed number: ')
#     if num == '' or num == '0':
#         return sumofnums
#     else:
#         return summ(sumofnums + int(num))
# print(summ())



    
















