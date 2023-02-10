#!/usr/bin/python3
""" to_json_string """
import json


def to_json_string(my_obj):
    """
        returns JSON representation of an object
        Args:
            my_obj: object to be converted to JSON
    """
    return json.dumps(my_obj)
