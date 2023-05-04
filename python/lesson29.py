# #1
# for i in range(5):
#     with open(f'new{i}.txt', 'w') as file:
#         file.write('Message')
# for i in range(5):
#     with open('new.txt', 'r') as file:
#         files = file.read()
#         print(files)
#2
# with open('second.txt', 'a') as file:
#     for i in range(101):
#         file.write(f'{i} \n')
# with open('second.txt', 'r') as file:
#     result = file.readlines()
#     print(''.join(result[:50]))
#  #3
# text = input('Enter the text you want to append to your file : ')
# with open('second.txt', 'a') as file:
#     file.write(text)
# with open('second.txt', 'r') as file:
#     result =file.readlines()
#     print(result[-1])
#4

# with open('second.txt', 'r') as file:
#     result =file.read().split()
#     result = sorted(result, key=len )
#     print(result[-1])

#5
# with open('second.txt', 'r') as file:
#     result =file.read()
#     s = '' 
#     for i in result:
#         if i in '1234567890':
#             s = s + i
#     print(s)

#6

# text = input('Enter the text you want to append to your file : ')
# with open('second.txt', 'a') as file:
#     file.write(text)
 
# with open('second.txt', 'r') as file:
#     result =file.readlines()
#     for i in range(len(result)):
#         if 'password' in  result[i].lower():
#             print('pass', result[i])
#         elif 'login' in result[i].lower():
#             print('log', result[i])

# import json
# info = {
#     'Name':'Lusine',
#     'Surname':'Petrosyan',
#     'Age': 19,
#     'Position': 'Student'
# }
# with open ('infoaboutme.json', 'w') as file:
#     json.dump(info, file, indent=4)
# with open ('infoaboutme.json', 'r') as file:
#     result = json.load(file)
#     print(result)
# text = input('Enter the needed : ')
# for k in result.keys():
#     if text == k:
#         print('yes')

