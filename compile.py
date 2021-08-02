import os

class Compile:
    """Compiler for B-Script"""
    def __init__(self):
        self.commands = {'var': self.var, 'env': self.env, 'show': self.show, 'end': self.end}

    def compile(self, code=str):
        break_ = code.find('>')
        command = code[:break_].replace(' ', '')

        if command in self.commands and break_ != -1:
            return self.commands[command](code=code[break_+1:].replace(' ', ''))
        else:
            if break_ == -1:
                return ['ERROR', '">" character not found in code.']
            return ['ERROR', 'Command ' + command + ' not found.']

    def var(self, code=str):
        return ['']

    def env(self, code=str):
        return ['']

    def show(self, code=str):
        print(code)
        return ['']

    def end(self, code=str):
        """
        Ends the program.
        :type code: object
        """
        return ['END', 'User ended with end.']


