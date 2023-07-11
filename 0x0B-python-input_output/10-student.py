#!/usr/bin/python3
"""student class"""


class Student:
    """student class"""

    def __init__(self, f_n, l_n, age):

        self.first_name = f_n
        self.last_name = l_n
        self.age = age

    def to_json(self, attrs=None):

        if type(attrs) == list:
            for attr in attrs:
                if type(attr) != str:
                    return {
                        k: getattr(self, k)
                        for k in attrs
                        if hasattr(self, k)
                    }
        return self.__dict__
