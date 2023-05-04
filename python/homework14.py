#146
# from random import choice
# dct ={ 
#     'B': [i for i in range(1, 16)],
#     'I': [i for i in range(16, 31)],
#     'N': [i for i in range(31, 46)],
#     'G': [i for i in range(46, 61)],
#     'O': [i for i in range(61, 76)],
# }
# for k, v in dct.items():
#     lst = []
#     while len(lst)<5:
#         random = choice(v)
#         if random not in lst:
#             lst.append(random)
#     print(k, lst)

# leetcode problem
# phone = {
#     "2": ['a','b','c'], 
#     "3": ['d','e','f'], 
#     "4": ['g','h','i'], 
#     "5": ['j','k','l'], 
#     "6": ['m','n','o'], 
#     "7": ['p','q','r','s'], 
#     "8": ['t','u','v'], 
#     "9": ['w','x','y','z']}
# digits = input('Enter the nums : ')
# combinations = phone[digits[0]]  #[a,b,c]

# for digit in range(1,len(digits)):
#     new_comb = []
#     for i in combinations:
#         for j in phone[digits[digit]]:                
#             new_comb.append(i+j)
#     combinations = new_comb    
# print(combinations)



# leetcode 43
# num1 = input('Enter the first number: ')
# num2 = input('Enter the second number: ')
# str_to_int = {
#     '1': 1,
#     '2': 2,
#     '3': 3,
#     '4': 4,
#     '5': 5,
#     '6': 6,
#     '7': 7,
#     '8': 8,
#     '9': 9,
#     '0': 0,
#     }
# result1 = 0
# for i in num1:
#     result1 = result1 * 10 +str_to_int[i]
# result2 = 0
# for i in num2:
#     result2 = result2 * 10 +str_to_int[i]
# answer = result2 * result1
# answerstr = ''
# while answer != 0:
#     digit = answer % 10
#     for k,v in str_to_int.items():
#         if v == digit:
#             answerstr = k + answerstr
#             break
#     answer = answer // 10
# print(answerstr)


#leetcode 205
# s = input('Enter the first : ')
# t = input('Enter the second : ')


# mydict = {}
# for a,b in zip(s , t):
#     mydict[a] = [b]
# print(mydict)











# s_dict = {}
# for i  in set(s):
#     s_dict[i] = s.count(i)
# t_dict = {}
# for i  in set(t):
#     t_dict[i] = t.count(i)
# print(sorted(s_dict.values()) == sorted(t_dict.values()))






# dct = {}
# text = input('Enter your text : ').lower()
# text = text.split()
# for word in text:
#     dct[word] = 0
# for word in text:
#     if word in dct:
#         dct[word] += 1
#     else:
#         dct[word] = 1
# maxval = max(dct.values())
# for k, v in dct.items():
#     if v == maxval:
#         print(k)











