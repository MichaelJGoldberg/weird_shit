def decode_v(input_str, key_word):
    _str = "abcdefghijklmnopqrstuvwxyz"
    n_list = input_str.replace(" ", "").lower()

    hor_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vert_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    input_list = [ ]
    key_list = [ ]
    fin_list = [ ]
    key_id_list = [ ]


    running = True

    i = 0
    j = 0
    k = 0

    for item in key_word:
        key_list.append(item)

    for item in n_list:
        input_list.append(item)

    #находятся идентефикаторы элементов ключа
    while i != len(key_list): 
        if key_list[i] == vert_list[j]:
            vert_value = vert_list[j]
            vert_id = vert_list.index(vert_value)
            key_id_list.append(vert_id)
            i = i + 1
            j = 0
        else:
            j = j + 1
            continue

    i = 0
    j = 0

    #выполняется непосредственное шифрование
    while len(fin_list) != len(input_list):
        if hor_list[i] == input_list[j]:
            if k < len(key_id_list):
                __value = hor_list[i]
                _id = hor_list.index(__value)
                fin_id = _id - key_id_list[k]
                if fin_id < 25:
                    fin_value = hor_list[fin_id]
                    fin_list.append(fin_value)
                    j = j + 1
                    k = k + 1
                    i = 0
                else:
                    fin_id = (fin_id - 25) - 1
                    __value = hor_list[fin_id]
                    fin_list.append(__value)
                    j = j + 1
                    i = 0
                    k = k + 1
            else:
                k = 0
                continue
        else:
            i = i + 1
            continue

    out_str = "".join(fin_list)
    print("       ","The result is:",out_str)

