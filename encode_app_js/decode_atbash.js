let in_list = prompt("Isert string: ")

in_list.split("")
let _list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
let r_list =['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
let f_list = [ ]
let i = 0
let j = 0
let _value = ""
let _id = 0

while (i != in_list.length)
{
    if (in_list[i] === r_list[j])
    {
        value = r_list[j]
        _id = r_list.indexOf(value)
        if (_id < 25)
        {
            _value = _list[_id]
            f_list.push(_value)
            i = i + 1
            j = 0
        }
        else
        {
            _id = _id - 25 - 1
            _value = _list[_id]
            f_list.push(_value)
            i = i + 1
            j = 0
        }
    }
    else
    {
        j = j + 1
    }
}

let str = f_list.join('')
alert(str)