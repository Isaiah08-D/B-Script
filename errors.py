# errors.py: Holds different errors that end the program.

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
