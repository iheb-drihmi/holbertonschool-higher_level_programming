#!/usr/bin/python3
'''json file'''
import json


def load_from_json_file(filename):
    '''Create a Python object from a JSON file.'''
    with open(filename) as myfile:
        return (json.load(myfile))
