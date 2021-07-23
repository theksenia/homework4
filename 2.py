import random
l= []; L1= []
for i in range(11):
    l.append(random.randint(0,105))
print(l)

L1=l  #список скопирован  иначе      L1=l.copy()
print(L1) #вывод скопированого списка
