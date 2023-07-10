#!/usr/bin/python3
"""inhertis from module"""


def inherits_from(obj, a_class):
    """check if object instance of class that
    inherited from the specified class or not
       Args:
           obj: object
           a_class: class
    """

    if type(obj) != a_class and isinstance(obj, a_class):
        return True
    return False
