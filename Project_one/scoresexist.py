# 4) Given the list below, look for the number 15, when you do, exit the loop.
from itertools import count

list= []
scores = [8, 13, 14, 15, 10, 9, 11, 14, 7, 12]
for n in scores:
    if(n==15):
     break
    else:
       print(n)
       list.append(n)
print(list)

    