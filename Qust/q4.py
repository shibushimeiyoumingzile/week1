import random

s = ''
str = 'qwertyuioplkjhgfdsazxcvbnm'
for i in range(1,1001):
    a = random.choice(str)
    s += a
set = set(s)

zd = {}
for i in set:
    zd[i] = s.count(i)

print(zd)