#!/usr/bin/python3
"""defines a file-appending function."""


def append_write(filename="", text=""):
    """append to file
        Arguments:
                 filename: filename
                 text: append text
    """
    with open(filename, "a", encoding="utf-8") as fi:
        return fi.write(text)
