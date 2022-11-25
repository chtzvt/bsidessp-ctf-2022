import sys
import textwrap 
import math

#key = "15c73a4dd082b02077da821258efd4be2d17eceb675f862c742cd4f910744c2bac30e46d11dec43673954376192291dc797ccac761b055d9476123611649cf3bd5e724e099"
key="15c73a4dd082b02077da821258efd4be2d17eceb675f862c742cd4f910744c2bac30e46d11dec43673954376192291dc797ccac761b055d9476123611649cf3bd5e724e099"
#key="249ce604d28e9d06459a623cb39"

def bspHASH(text):
    s = str()
    for t in text:
        s = s + str(ord(t)*len(text)) + "12345"
    return hex(int(s)).replace("0x", "")
"""
        print(len(text))
        print(str(ord(t)*len(text)))
        print(str(ord(t)*len(text)) + "12345")
"""
"""
        print(int(s))
        print(hex(int(s)))
"""
    

def factors(x):
   f = []
   for i in range(1, x + 1):
       if x % i == 0:
           f.append(i)
   return f

if __name__ == '__main__':

    key_dec = str(int("0x" + key, 0))

    chars = key_dec.split('12345')
    chars.pop(len(chars) - 1)

    print(chars)

    vals = []
    for c in chars:
        #vals.append((chr(int(int((int("0x" + c, 0) - 12345) / len(chars) / 100000)))))
        #vals.append(chr(int(((int(c)) / key_len) / 100000.0)))
        vals.append(chr(int(int(c) / len(chars))))

    print(''.join(vals))

    """
    key_len = 15

    for f in factors:
        print("Trying " + str(f))
        vals = []
        chars = [key[i:i+9] for i in range(0, len(key), 9)]

        try:
            for c in chars:
                vals.append((chr(int(int((int("0x" + c, 0) - 12345) / f) / 100000))))
            
            15c73aprint(''.join(vals))
        except Exception as e:
            print(e)
    """


"""
    for c in chars:


(char - 12345) / 6
"""