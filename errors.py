# errors.py: Holds different errors that end the program.
import setup
import sys


class Error:
    def __init__(self, message, end=False):
        print('ERROR:\n' + str(message))

        if end:
            sys.exit()


class SyntaxError:
    def __init__(self, message, end=False):
        print('SYNTAX ERROR:\n' + str(message))

        if end:
            sys.exit()

class InvalidPath:
    def __init__(self, message, end=False):
        print('INVALID PATH ERROR:\n' + str(message))

        if end:
            sys.exit()
