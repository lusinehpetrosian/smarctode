digits = [1,2,3]
s = ''
for i in digits:
    s = s + str(i)
    s = int(s)

print(list(str((int(s) + 1)), type = int))