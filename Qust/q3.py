import random

list = []
for i in range(1,21):
    a = random.randint(1,10)
    list.append(a)

print(list)
li = sorted(list[::2],reverse=True)
print(li)