import os

class Compile:
    """Compiler for B-Script"""
    def __init__(self):
        self.commands = {'var': self.var, 'env': self.env, 'show': self.show, 'end': self.end, 'get': self.get, 'python': self.python}

    def compile(self, code=str, vars=type, **kwargs):
        """
        Compiles code.
        :param code: line of code
        :param vars: vars.Vars class
        :return:
        """

        self.vars = vars

        break_ = code.find('>')
        command = code[:break_].replace(' ', '')

        if command in self.commands and break_ != -1:
            return self.commands[command](code=code[break_+1:].replace(' ', ''))
        else:
            if break_ == -1:
                return ['ERROR', '">" character not found in code.']
            return ['ERROR', 'Command ' + command + ' not found.']

    def var(self, code=str):
        """
        Set or change a variable.
        """
        break_ = code.find('>') # find the index of where the secound argument is placed
        if break_ == -1:
            return ['ERROR', 'Could not find second ">" character. ">" needed before second argument.']

        return ['']

    def get(self, code=str):
        """Get a variable."""

    def env(self, code=str):
        return ['']

    def show(self, code=str):
        if 'get>' in code.strip(' '): # if the show command might need to show a variable
            x = Compile()
            y = x.compile(code)
            if y[0] == 'ERROR': # if it doesn't need to show a variable or if there is an error in the statement
                print(code)
                return ['', '']
            print(y)

        else:
            print(code)
        return ['', '']

    def end(self, code=str):
        """
        Ends the program.
        :type code: object
        """
        return ['END', 'User ended with end.']
    def python(self, code=str):
        """
        Runs a python file
        :param code:
        :return:
        """
        os.system('')


