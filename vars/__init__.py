import os
from . import types


class Vars:
    def __init__(self):
        self.vars = {}

    def add(self, k, v):
        data_type = None
        if v[0:1] == '[' and v[-2:-1] == ']':  # if it's a list
            v = types.List(v)
        else:
            v = types.String(v)
        self.vars[k] = v

    def view(self, k):
        return self.vars[k]

    def data_type(self, k):
        data = self.vars[k]
        return type(data)
