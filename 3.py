import random
l1 = list()
l2 = list()
l = list()
m1= []
m2= []
for _ in range(0, 8):
    l1.append(random.randint(0, 10))
    l2.append(random.randint(0, 10))

for j in l1:
    if j not in m1:
        m1.append(j)
print(m1)

for j1 in l2:
    if j1 not in m2:
        m2.append(j1)
print(m2)

for i_l1 in m1:
     for i_l2 in m2:
         if i_l1 == i_l2 and i_l1 not in l:
             l.append(i_l2)
l1.clear()
l2.clear()
for d in m1:
    if not (d in m2):
        l1.append(d)

for d1 in m2:
    if not (d1 in m1):
        l2.append(d1)
print (l1+l2)