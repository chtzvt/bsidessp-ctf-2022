import sys

def bspHASH(text):
    s = str()
    for t in text:
        print(str(ord(t)*len(text)) + "12345")
        s = s + str(ord(t)*len(text)) + "12345"

    print(len(text))
    print(len(s))
    print(len(s) / len(text) == 9)

    print(int(s))
    print(len(hex(int(s)).replace("0x", "")))

    print("--------")

    return hex(int(s)).replace("0x", "")

if __name__ == '__main__':
    print(bspHASH(sys.argv[1]))

