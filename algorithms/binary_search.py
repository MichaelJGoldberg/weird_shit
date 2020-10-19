import random
from itertools import groupby

_list = []
for i in range (1, 100):
    j = random.randint(1,101)
    _list.append(j)
_list.sort()
new_list = [el for el, _ in groupby(_list)]
print (new_list)
highest = len(new_list)
lowest = 0


item = random.randint(1, highest)
#item = int(input(":"))
print(item)
while True:
    mid = round((highest - lowest)/2+lowest)
    if mid > item:
        print(mid, "много")
        highest = mid
    if mid < item:
        print(mid, "мало")
        lowest = mid
    if mid == item:
        print("Item =", item, "Guess =", mid, "ID =", new_list.index(mid))
        break
    if lowest > highest:
        print("No value")
        break





    



    
