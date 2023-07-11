#!/usr/bin/python3
"""from json to obj"""


import json


def from_json_string(my_str):
    """from json to string
        Args:
            my_str: string to convert
    """
    return json.loads(my_str)
