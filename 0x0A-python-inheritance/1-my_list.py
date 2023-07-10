#!/usr/bin/python3
"""Mylist module"""


class MyList(list):
    """Mylist class"""

    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
