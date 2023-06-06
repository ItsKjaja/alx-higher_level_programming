#!/usr/bin/python3


def uppercase(str):
    for j in range(len(str)):
        i = ord(str[j])
        if (i >= 97) and (i <= 122):
            i -= 32
            print("{}".format(chr(i)), end="")
            print()
