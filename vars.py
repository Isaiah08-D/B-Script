import os

class Vars:
    def __init__(self):
        self.vars = {}
    def add(self, k, v):
        self.vars[k] = v
    def view(self, k):
        return self.vars[k]
