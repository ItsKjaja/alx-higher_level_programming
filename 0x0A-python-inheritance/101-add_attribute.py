#!/usr/bin/python3
"""this module defines a function that adds attribute to objects"""


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible
    """

    if not hasattr(obj, ""__dic__""):
        raise TypeError("can't add new attribute")
    setettr(obj, att, value)
