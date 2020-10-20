from random import randint
crcls = int(input("Print amount of circles: "))+1
_max = int(input("Print the maximum rendom number of: "))+1
array = [ ]
j = 0
i = 0
k = 1

for i in range(1, crcls):
    j = randint(1,_max)
    array.append(j)

j = 1
i = 0

print(array)

def bubble_up(arr):
    k = 1
    i = 0
    j = 1
    while k != len(arr)-1:
        if j < len(arr):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i = i + 1
                j = j + 1

            else:
                k = k + 1
                i = i + 1
                j = j + 1

        else:  
            return arr


def bubble_down(arr):
    i = len(arr)-2
    j = len(arr)-1
    k = 1
    while k != len(arr)-1:
        if j >= 1:
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i = i - 1
                j = j - 1
            else:
                k = k + 1
                i = i - 1
                j = j - 1
        else: 
            return arr


def shaking(arr):
    k = 1
    i = 0
    j = 1
    while k != len(arr)-1:
        if j < len(arr):
            if arr[i] > arr[j]:
                bubble_up(arr)
                bubble_down(arr)
                i = i + 1
                j = j + 1
                print(arr)

            else:
                k = k + 1
                i = i + 1
                j = j + 1

        else: 
            i = 0
            j = 1
            k = 0  
    print( arr )   


shaking(array)
