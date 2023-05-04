# height = eval(input('Enter your list of height  : '))
# firstind = 0
# lastind = len(height)-1
# maximum = 0
# while firstind<lastind:
#     area = (lastind - firstind) * min(height[firstind], height[lastind])
#     maximum = max(area, maximum)
#     if height[firstind] < height[lastind]:
#         firstind += 1
#     else:
#         lastind -= 1
# print(maximum)

#1
# from pprint import pprint
# variances = {
#     1: 'a',
#     2: 'b', 
#     -5: 'c',
#     4: 'd',
# }
# items = dict(sorted(variances.items()))
# print(items)

 #2
# variances = {
#     'a': 1,
#     'b': 2,
#     'c':-5,
#     'd': 4,
# }
# items = list(variances.items())
# for i in range(len(items)):
#     items[i] = (items[i][1], items[i][0])
# items = sorted(items)

# for i in range(len(items)):
#     items[i] = (items[i][1], items[i][0])
# print(dict(items))

# #3
# mydict = {
#     'name':1,
#     'surname':2,
# }
# keyinput = input('Enter the key : ')
# print(mydict.get(keyinput, 'There is no such item!'))

#4
# dict1 = {'a':50, 'b':700}
# dict2 = {'c':40, 'd':600}

# dict1.update(dict2)
# print(dict1)

#5
# dict1 = {'a':50, 'b':70}
# dict2 = {'b':40, 'd':600}
# for i in dict1:
#     if i in dict2:
#         dict2[i] += dict1[i]
# dict1.update(dict2)
# print(dict1)

#137
# from pprint import pprint
# from random import randint
# dct = {
#     2: 0,
#     3: 0,
#     4: 0,
#     5: 0,
#     6: 0,
#     7: 0,
#     8: 0,
#     9: 0 ,
#     10: 0,
#     11: 0,
#     12: 0,
# }
# for _ in range(1000):
#     case1 = randint(1,6)
#     case2 = randint(1,6)
#     dct[case1 + case2] += 1
# for i in dct:
#     dct[i] = dct[i]/10
# pprint(dct)









