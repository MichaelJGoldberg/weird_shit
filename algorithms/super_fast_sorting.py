from random import randint

crcls = int(input("Print amount of circles: "))+1
_max = int(input("Print the maximum rendom number of: "))+1

arr = [ ]

for i in range(1, crcls):
    j = randint(1,_max)
    arr.append(j)

def quicksort(array): 
    if len(array) < 2:
        return array
    else: 
        pivot = array[0]
        less = [i for i in array if i < pivot]
        greater=  [ i for i in array if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater) 

print (quicksort(arr))