from decode_ceasar import decode
from encode_ceasar import encode
from crack import cracker
from freq import crack_o
ctrl = " "
ctrl1 = " "
running = True
print(" ","\t***!!!WElCOME TO THE CEASER SCHIFRE SIMULATOR!!!***\t")
print(" ","\tHERE U CAN ENCODE OR DECODE\t")

while running:
    ctrl = str(input(" \tWHAT DO U, WANT TO DO(en, de, cr1, cro): "))

    if ctrl == "en":
        __str = str(input(" \tPrint the frase to encode: "))
        __key = int(input(" \tPrint the key: "))
        encode(__str, __key)

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



