#!/usr/bin/python3
for i in range(0, 9):
    for n in range(1, 10):
        if n > i:
            if i != 8:
                print("{}{}, ".format(i, n), end="")
            else:
                print("{}{}".format(i, n))
