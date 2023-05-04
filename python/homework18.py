#174
# def g_c_d(a,b):
#     if b == 0:
#         return a
#     else:
#         c = a%b
#         return g_c_d(b,c)
# a =int(input('Enter a: '))
# b = int(input('Enter b: '))
# print(g_c_d(a,b))

#175
# def binary(n):
#     if int(n) == 0 or int(n) == 1:
#         return n
#     else:
#         return str(binary(int(n)//2)) + str(int(n)%2)
# n = input('Enter your number: ')
# if n[0] == '-':
#     print('Invalid input! Ypu have to input only positive numbers!')
# else:
#     print(binary(n))

#176
# def nato(s):
#     natodct= {
#         'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
#         'E': 'Echo', 'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel',
#         'I': 'India', 'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
#         'M': 'Mike', 'N': 'November', 'O': 'Oscar', 'P': 'Papa',
#         'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
#         'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'Xray',
#         'Y': 'Yankee', 'Z': 'Zulu',
#     }
#     if len(s) == 0:
#         return s
#     else:
#         if s[0].isalpha():
#             return natodct[s[0]] +' ' + nato(s[1:])
#         else: 
#             return s[0] + ' ' + nato(s[1:])
# s = input('Enter your string: ').upper()
# print(nato(s))
#177

# def roman(s):
#     romandct = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
#     if len(s) == 0:
#         return 0
#     elif len(s) == 1:
#         return romandct[s[0]]
#     if romandct[s[1]] > romandct[s[0]]:
#         return roman(s[2:]) + romandct[s[1]] - romandct[s[0]]
#     else:
#         return roman(s[1:]) + romandct[s[0]]
# s = input('Enter your string : ')
# print(roman(s))


#178
# def recursion(s):
#     if len(s) == 0 or len(s) == 1:
#         return s
#     else:
#         return s[-1] + recursion(s[1:-1]) + s[0]
# s = input('Enter the string: ')
# print(s == recursion(s)) 
# print(recursion(s))

#179
# def square_root(n,guess = 1.0):
#     if abs(guess**2 - n) < 1E-12:
#         return guess
#     else:
#         return square_root(n, (guess + n/guess)/2)
# n = int(input('Enter the number: '))
# print(square_root(n))

#180
# def editdis(s,t):
#     if len(s) == 0:
#         return len(t)
#     elif len(t) == 0:
#         return len(s)
#     else:
#         cost = 0
#         if s[-1] != t[-1]:
#             cost = 1
#         d1 = editdis(s[:-1], t ) + 1
#         d2 = editdis(s, t[:-1]) + 1
#         d3 = editdis(s[:-1], t[:-1]) + cost
#         return min(d1,d2,d3)
# s = input('Enter the first string! ')
# t = input('Enter the second string! ')
# print(editdis(s,t))

#184

# def flattening(data):
#     if data == []: return []
#     elif isinstance(data[0], list):  return flattening(data[0]) + flattening(data[1:])
#     else: return [data[0]] + flattening(data[1:])
# print(flattening([1, [2, 3], [4, [5, [6, 7]]],[[[8], 9], [10]]]))
