from encode_ceasar import encode
from decode_ceasar import decode
from crack import cracker
from freq import crack_o

from encode_vigeneur import encode_v
from decode_vigeneur import decode_v

from encode_atbash import encode_atb
from decode_atbash import decode_atb



ctrl = " "
ctrl1 = " "
running = True
print(" ","\t***!!!WElCOME TO THE SCHIFRE SIMULATOR!!!***\t")
print(" ","\tHERE U CAN ENCODE OR DECODE\t")

while running:
    ctrl = str(input(" \tWHAT DO U, WANT TO DO(en, en_v, de, de_v, cr1, cro, en_a, de_a): "))

    if ctrl == "en":
        __str = str(input(" \tPrint the frase to encode: "))
        __key = int(input(" \tPrint the key: "))
        encode(__str, __key)

    if ctrl == "en_v":
        __str = str(input(" \tPrint the frase to encode: "))
        __key = str(input(" \tPrint the key: "))
        encode_v(__str, __key)

    if ctrl == "en_a":
        __str = str(input(" \tPrint the frase to encode: "))
        encode_atb(__str)

    if ctrl == "de_a":
        __str = str(input(" \tPrint the frase to decode: "))
        decode_atb(__str)

    if ctrl == "de_v":
        __str = str(input(" \tPrint the frase to decode: "))
        __key = str(input(" \tPrint the key: "))
        decode_v(__str, __key)

    if ctrl == "de":
        __str = str(input(" \tPrint the frase to decode: "))
        __key = int(input(" \tPrint the key: "))
        decode(__str, __key)

    if ctrl == "cr1":
        __str = str(input(" \tPrint the frase to crack: "))
        cracker(__str)
    
    if ctrl == "cro":
        __str = str(input(" \tPrint the frase to crack_o: "))
        crack_o(__str)

    ctrl1 =str(input (" \tDO U WANT TO CONTINUE?????!!!(y, n)"))

    if ctrl1 == "y":
        print("\n")
        continue
    if ctrl1 == "n":
        break



