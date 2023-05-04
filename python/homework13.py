#136
# dct = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5, 
#     'f': 1,
#     'g': 2,
#     'h': 3,
#     'i': 4,
#     'j': 5,
# }
# value = int(input('enter the value: '))
# valuekeys = []
# for key in dct.keys():
#     if dct[key] == value:
#         valuekeys.append(key)
# print(valuekeys)
# ____________________________________________2nd type ____________________________________________
# for k,v in dct.items():
#     if v == value:
#         print(k)
#         break

#138
# dct = {
#     ' ': '0',
#     '.': '1',
#     ',': '11',
#     '?': '111',
#     '!': '1111',
#     ':': '11111',
#     'a': '2',
#     'b': '22',
#     'c': '222',
#     'd': '3',
#     'e': '33',
#     'f': '333',
#     'g': '4',
#     'h': '44',
#     'i': '444',
#     'j': '5',
#     'k': '55',
#     'l': '555',
#     'm': '6',
#     'n': '66',
#     'o': '666',
#     'p': '7',
#     'q': '77',
#     'r': '777',
#     's': '7777',
#     't': '8',
#     'u': '88',
#     'v': '888',
#     'w': '9',
#     'x': '99',
#     'y': '999',
#     'z': '9999',
# }
# text = input('Enter the text : ').lower()
# string = ''
# for i in text:
#     string += dct[i]
# print(string)




#139
# dct = {
#     'a': '.-',
#     'b': '-...', 
#     'c': '-.-.', 
#     'd': '-..', 
#     'e': '.', 
#     'f': '..-.', 
#     'g': '--.',
#     'h': '....', 
#     'i': '..', 
#     'j': '.---', 
#     'k': '-.-', 
#     'l': '.-..', 
#     'm': '--', 
#     'n': '-.',
#     'o': '---', 
#     'p': '.--.', 
#     'q': '--.-', 
#     'r': '.-.', 
#     's': '...', 
#     't': '-', 
#     'u': '..-',
#     'v': '...-', 
#     'w': '.--', 
#     'x': '-..-', 
#     'y': '-.--', 
#     'z': '--..', 
#     '0': '-----',
#     '1': '.----', 
#     '2': '..---', 
#     '3': '...--', 
#     '4': '....-', 
#     '5': '.....', 
#     '6': '-....',
#     '7': '--...', 
#     '8': '---..', 
#     '9': '----.',
# }

# text = input('Enter the text : ').lower()
# string = ''
# for i in text:
#     if i in dct:
#         string += dct[i]
# print(string)

#140
# dct = {
#     'A': 'Newfoundland',
#     'B': 'Nova Scotia',
#     'C': 'Prince Edward Island',
#     'E': 'New Brunswick',
#     'G': 'Quebec',
#     'H': 'Quebec',
#     'J': 'Quebec',
#     'K': 'Ontario',
#     'L': 'Ontario',
#     'M': 'Ontario',
#     'N': 'Ontario',
#     'P': 'Ontario',
#     'R': 'Manitoba',
#     'S': 'Saskatchewan',
#     'T': 'Alberta',
#     'V': 'British Columbia',
#     'X': 'Nunavut or Northwest Territories',
#     'Y': 'Yukon'
# }

# code = input('Enter the postal code')
# if code[0] in 'DFIOQUWZ' or len(code) != 6:
#     print('Invalid input!')
# if code[1] == 0:
#     address = 'rural'
# else:
#     address = 'urban'
# provinces = dct[code[0]]
# print(f'the postal code is for a {address} address in {provinces}')

#142
# string = input('Enter the string')
# soue = set(string)
# print(len(soue))


#143
# word1 = input('Enter the first word: ')
# word2 = input('Enter the second word: ')
# word1 = list(word1)
# word2 = list(word2)
# print(sorted(word2) == sorted(word1))
# ___________________________________2nd type________________
# print(sorted(word1)==sorted(word2))

#144
# sentence1 = input('Enter the first sentence: ').lower()
# sentence2 = input('Enter the second sentence: ').lower()
# syms = list('!@#$%^&*()_+:,<>?[]{}. ')
# for i in syms:
#     sentence1 = sentence1.replace(i,'')
#     sentence2 = sentence2.replace(i,'')
# sentence1 = list(sentence1)
# sentence2 = list(sentence2)

# print(sorted(sentence2) == sorted(sentence1))

#145
# dct = {
#     1: 'AEILNORSTU',
#     2: 'DG',
#     3: 'BCMP',
#     4: 'FHVWY',
#     5: 'K',
#     8: 'JX',
#     10: 'QZ',
# }
# result = 0
# word = input('Enter the word: ').upper()
# for char in word:
#     for k,v in dct.items():
#         if char in v:
#             result += k
# print(result)

#146
from random import choice
dct ={ 
    'B': [i for i in range(1, 16)],
    'I': [i for i in range(16, 31)],
    'N': [i for i in range(31, 46)],
    'G': [i for i in range(46, 61)],
    'O': [i for i in range(61, 76)],
}
for k, v in dct.items():
    lst = []
    while len(lst)<5:
        random = choice(v)
        if random not in lst:
            lst.append(random)
    print(k, lst)

    