#для взлома грубой силой необходимо проверить каждый ключ в алгоритме
def cracker(_str):
    n_list = _str.replace(" ", "")
    end_list = []
    _list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t","u","v","w","x", "y","z" ]
    i = 0
    j = 0
    _id = 0
    key = 1
    cnt = 1
    while key < 27:
        while j != len(n_list):
            if _list[i] == n_list[j]:
                lit = _list[i]
                _id = _list.index(lit) - key
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
        __str = "".join(end_list)
        __str.lstrip(" ")
        print("\n","       ","The result", cnt ,"is:",__str,"\n") 
        j = 0
        i = 0
        __str = " "
        end_list = [ ]
        cnt = cnt + 1
        key = key + 1


