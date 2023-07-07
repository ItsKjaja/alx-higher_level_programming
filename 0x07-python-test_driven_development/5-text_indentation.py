#!/usr/bin/python3
"""

Function that prints a text with 2 new lines after each of these charachters:
    . ? and :
"""


def text_indentation(text):
    """
    Prints a text replace some characters with 2 newlines

    Args:

    text: must be a string

    if not a string a TypeError is raised

    there is no space at the begining at the end of each printed line

    """

    if not isinstance(text, str):
        msg = "text must be a string"
        raise TypeError(msg)

    if len(text) == 0:
        print(end='')
        return None

    textlist = []
    mark = 0

    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            textlist.append(text[mark: i + 1] + "\n\n")
            mark = i + 1

    textlist = [i.strip(' ') for i in textlist]

    new_text = "".join(textlist)

    print(new_text, end='')
