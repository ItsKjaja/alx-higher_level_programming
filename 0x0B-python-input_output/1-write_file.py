#!/usr/bin/python3
"""write to file"""


def write_file(filename="", text=""):
    """write to file
       Arguments:
                filename: filename
                text: text to write
    """
    with open(filename, "w") as f:
        return f.write(text)
