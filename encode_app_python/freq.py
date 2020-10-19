from collections import Counter
from decode_ceasar import decode

def crack_o(_str):
    arr = []
    _str = _str.replace(" ","").lower()
    for char in _str:
        arr.append(char)
    _list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t","u","v","w","x", "y","z" ]
    ctrl = 0
    i = 0
    j = 0
    _nlist = [ ]
    arr.sort()
    count = Counter(arr)

    max_value = max(count.values())
    final_dict = {k: v for k, v in count.items() if v == max_value}
    end_list = []
    for item in final_dict:
        _nlist.append(item)

    key = 0

    while True:
        if _list[j]== _nlist[i]:
            _j = _list[j]
            key = _list.index(_j) - _list.index("o")
            break
        else:
            j = j + 1
            continue
    j = 0
    i = 0
    decode(_str , key)












    



