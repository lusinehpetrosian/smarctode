#35
# n = int(input('Enter the number:: '))
# if n % 2 == 0:
#     print('Even')
# else:
#     print('Odd')

#36
# human = int(input('Human age is '))
# if 0 <= human <= 21:
#     print('Dog', human // 10.5)
# elif human > 21:
#     print('Dog', 2 + (human - 21)//4)
# else:
#     print('Invalid value!!!')

#37
# char = input('Enter the character: ').lower()
# vowel  = 'auoiAUOI'
# consonant = 'qwrtypsdfghjklzxcvbnm'
# if char in vowel:
#     print('vowel')
# elif char in consonant:
#     print('Consonant')    
# else:
#     print('Invalid Input')    

#38
# n = int(input('The number of angles::: '))
# if n == 3:
#     print('This is triangle!')
# elif n==4:
#     print('This is quadrilateral!')
# elif n==5:
#     print('This is pentagon!')
# elif n==6:
#     print('This is hexagon!')
# elif n==7:
#     print('This is heptagon!')
# elif n==8:
#     print('This is octagon!')
# elif n==9:
#     print('This is nonagon!')
# elif n==10:
#     print('This is decagon!')
# else:
#     print('INVALID INPUT!!!!!!!!!!') 

#39
# m = input('Month is :::')
# if m == 'january' or m == 'march' or m == 'may' or m == 'july' or m == 'august':
#     print('Days = ', 31)
# elif m == 'april' or m == 'june' or m == 'september':
#     print('Days = ', 30)
# elif m == 'february':
#     print('Days = 28')

#40
# n = float(input('Noise level in db :'))
# if n == 130:
#     print('Jack hammer')
# elif n == 106:
#     print('Gas Lawnmower')
# elif n == 70:
#     print('Alarm Clock')
# elif n == 40:
#     print('Quiet Room')
# elif n < 40:
#     print('Sound level is low!')
# elif n > 130:
#     print('Sound level is high!')
# elif 40 < n < 70:
#     print('Sound level is between Jack hammer and Gas Lawnmower')
# elif 70 < n < 106:
#     print('Sound level is between Gas Lawnmower and Alarm Clock')
# elif 106 < n < 130:
#     print('Sound level is between Alarm Clock and Quiet Room')


#3
# year = int(input('Year is: '))
# if year % 4 == 0 and year % 10 != 0:
#     print('Yes!!')
# elif year < 0:
#     print('Invalid input!')
# else:
#     print('No!!!') 

#4
from random import randint
a = randint(0,5)
player1 = int(input(" player 1 input the digit!"))
score1 = 0
player2 = int(input(" player 2 input the digit!"))
score2 = 0
if player1 == a:
    score1 +=1
elif player2 ==a:
    score2 +=1
else:
    print('LOSERS!!!!')
if score1 == 2:
    print("player  1 won")
elif score2 ==2:
    print('Player 2 won')

