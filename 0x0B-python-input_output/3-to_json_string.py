#!/usr/bin/python3
""" obj to json"""

import json


def to_json_string(my_obj):
    """ convert object to json
       Args:
           my_obj: object
    """
    return json.dumps(my_obj)
