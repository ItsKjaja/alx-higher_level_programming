#!/usr/bin/python3
"""Defines a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containig a given string in a file.
    Args:
        filename (str): the name of the file.
        search_string (str): the string to search for within the file.
        new_string (str): the string to insert.
    """
    text = ""
    with open(filename) as fi:
        for line in fi:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as wo:
        wo.write(text)
