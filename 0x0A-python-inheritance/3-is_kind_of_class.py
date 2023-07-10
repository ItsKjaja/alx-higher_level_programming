#!/usr/bin/python3
"""is kind of class module"""


def is_kind_of_class(obj, a_class):
    """check if obj instance of class.
       Arguments:
                obj: object
                a_class: class
    """
    if isinstance(obj, a_class):
        return True
    return False
