import random
l= [] ; m= []
for i in range(10):
    l.append(random.randint(0,9))
print(l)

for j in l:
    if j not in m:
        m.append(j)
print(m)
