import os
from . import types
import setup

class Vars:
    def __init__(self):
        self.vars = {}

    def add(self, k, v):
        data_type = None
        if v[0:1] == 's':  # if it's a string
            v = types.String(v[1:])  # creates a string [1:] removes the s character
        elif v[0:1] == 'l':  # list
            v = types.List(v[1:])  # create a list [1:] removes the l character
        elif v[0:1] == 'i': # integer
            v = types.Integer(v[1:]) # creates a integer [1:] removes the i character
        self.vars[k] = v

    def get(self, k):
        return self.vars[k]

    def data_type(self, k):
        data = self.vars[k]
        return type(data)
