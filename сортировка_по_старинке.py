from random import randint

arr = []
arr_copy = arr
cnt = int(input("Print how much:"))+1
for i in range (1, cnt):
    j = randint(1, 100)
    arr.append(j)

print(arr)
arr_copy = arr
new_arr= []
smallest = 0
i = 0

while True:
    if i != len(arr):
        if arr[i] < smallest:
            value = arr[i]
            new_arr.append(value)
            if len(arr)>1:
                del arr[i]
            else:
                break
            smallest = value - 1
            i = len(arr)
        else:
            i = i + 1
    else:
        smallest = smallest + 1
        i = 0

print(new_arr)
