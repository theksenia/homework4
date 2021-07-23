import random
l1 = list()
l2 = list()
l  = list()
a= list()
for _ in range(0, 5):
    l1.append(random.randint(0, 5))
    l2.append(random.randint(0, 8))
for i in l1: print(i, end=" ")
print("\n")
for i in l2: print(i, end=" ")

a = l1+l2

for i_l1 in l1:
     for i_l2 in l2:
         if i_l1 == i_l2 and i_l1 not in l:
             l.append(i_l2)

print("\n")
print(l)