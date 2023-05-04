pattern = 'abba'
s = 'dog cat cat dog'
s = s.split()
dct = {}
for k,v in zip(pattern, s):
    if k in dct and v != dct[k]:
        return False 
    dct[k] = v

print(dct)

def isUgly(self, n: int) -> bool:
        ls = []
        i = 2
        if n==1:
            return True
        while n!=1:
            if n % i == 0:
                ls.append(i)
            while n % i == 0:
                n = n//i
            else:
                i +=1
        if set((sorted(ls))) not in [{2},{3},{5},{2,3},{2,5},{3,5},{2,3,5}]:
            return False
        else:
            return True
        
