_str = str(input("Print the frase to encode:")).lower()
key = int(input ("Print your key: "))
n_list = _str.replace(" ", "")
end_list = []
_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t","u","v","w","x", "y","z" ]
i = 0
j = 0
_id = 0
while j != len(n_list):
    if _list[i] == n_list[j]:
        lit = _list[i]
        _id = _list.index(lit) + key
        if _id < 25:
            value = _list[_id]
            end_list.append(value)
            j = j + 1
            i = 0
        else:
            _id = (_id - 25) - 1
            value = _list[_id]
            end_list.append(value)
            j = j + 1
            i = 0

    else:
        i = i + 1

for item in end_list:
    print(item, end = "")     









