#!/usr/bin/python3
"""defines a text file-reading function"""


def read_file(filename=''):
    """function that reads a text file (UTF8) and prints it to stdout"""

    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
