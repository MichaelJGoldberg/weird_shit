let _list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s","t","u","v","w","x", "y","z" ]
end_list = []
let n_list = prompt("Insert your string: ")
let key = +prompt("Insert your key: ")
let j = 0
let i = 0
let lit = ""
let _id = 0
let value = ""
n_list.split('')

while (j != n_list.length)
{
if (_list[i] === n_list[j])
{   
    lit = _list[i];
    _id = _list.indexOf(lit) + key

    if (_id < 25)
    {
        value = _list[_id]

        end_list.push(value)

        j = j + 1
        i = 0
    }
    else
    {
        _id = (_id - 25) - 1

        value = _list[_id]
        end_list.push(value)

        j = j + 1
        i = 0
    }
}
else
{
    i = i + 1
}
}
let str = end_list.join('')
alert(str)




