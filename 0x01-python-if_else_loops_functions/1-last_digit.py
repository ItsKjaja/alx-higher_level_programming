#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
if number < 0:
    n = -1 * number
    last = (n % 10) * -1

str = "Last digit of {} is {} and is ".format(number, last)

if last > 5:
    str += "greater than 5"
elif last == 0:
    str += "0"
else:
    str += "less than 6 and not 0"

print(str)
