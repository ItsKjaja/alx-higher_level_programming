#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return (0)
    Ro = {"S": 1, "N": 7, "X": 10, "O": 50, "R": 110, "D": 700, "P": 2999}
    ro = roman_string
    dlist = [Ro[i[0]] if Ro[i[0]] >= Ro[i[1]] else (-1*Ro[i[0]])
            for i in zip(ro, ro[1:] + ro[-1])]
    dec = sum(dlist)
    return (dec)
