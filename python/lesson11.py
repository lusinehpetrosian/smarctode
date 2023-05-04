#83
# from random import randint
# maximum= -1
# k = 0
# for i in range(100):
#     number = randint(1,100)
#     if number <= maximum:
#         print(number)
#     elif number > maximum:
#         maximum = number
#         k += 1
#         print(number, '<== Here was an update')
# print(f'maximum number is {maximum}\nThe number of updates is {k}')

#84
# from random import choice
# cases = 'o', 'p'
# k = 0 
# for i in range(10):
#     string = ''
#     while True:
#         choiceis = choice(cases)
#         string = string + choiceis
#         if len(string) >=3 and string[-1] == string[-2] == string[-3]:
#             print(string,'The attempts number is ', len(string))
#             k += len(string)
#             break
# print(f'Probable number of ateempts is {k/10}')

#84 second type of solution
from random import choice
variance = 'op'
all_steps = 0
for i in range(10):
    coin = choice(variance)
    print(coin, end = ' ')
    counter = 1
    one_step = 0
    while counter != 3:
        one_step += 1
        new_try = choice(variance)
        print(new_try, end = ' ')
        if new_try == coin:
            counter += 1
        else:
            counter == 1
        coin = new_try
        print(f'({one_step} tries)')
print(f'Main point is {all_steps/10}')





