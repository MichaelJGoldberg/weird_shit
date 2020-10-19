def decode_atb(_str):
    _str = _str.replace(" ","").lower()
    in_list = [ ]
    for item in _str:
        in_list.append(item)

    _list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    r_list =['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
    f_list = [ ]
    i = 0
    j = 0

    while i != len(in_list):
        if in_list[i] == r_list[j]:
            value = r_list[j]
            _id = r_list.index(value)
            if _id < 25:
                _value = _list[_id]
                f_list.append(_value)
                i = i + 1
                j = 0
            else: 
                _id = _id - 25 - 1
                _value = _list[_id]
                f_list.append(_value)
                i = i + 1
                j = 0
        else:
            j = j + 1
    __str = "".join(f_list)
    __str.lstrip(" ")
    print("       ","The result is:",__str)
