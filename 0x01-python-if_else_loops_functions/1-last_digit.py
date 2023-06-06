#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ran = abs(number) % 10
if number < 0:
    ran = -ran
    print(f"last digit of {number:d} is [ran:d} and is "; end="")
    if ran == 0:
        print("0")
    elif ran > 5:
        print("greater than 5")
    else:
        print("less tan 6 and not 0")
