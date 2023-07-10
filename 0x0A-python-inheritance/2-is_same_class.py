#!/usr/bin/python3
"""is same class module"""


def is_same_class(obj, a_class):
    """check if obj instance of class
    Arguments:
             obj: object
             a_class: class
    """

    if type(obj) == a_class:
        return True
    return False
