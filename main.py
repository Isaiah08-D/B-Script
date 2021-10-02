from vars import Vars
from compile import Compile
import os
import setup
PATH = os.path.expanduser('~').split('\\')

vars = Vars()
compile = Compile()
setup.quickConfig()

while True:
    code = input('\\'.join(PATH)+": ")
    t = compile.compile(vars, code, PATH)
    if t[0] == 'END':
        print('END')
        break
    elif t[0] == 'VAR':
        if t[1][0] == 'def':  # if the user is defining a new function or changing a variable completely

            vars.add(t[1][1], t[1][2])
    elif t[0] == 'PATH': # if the comamnd is something related to the directory
        if t[1][0] == '+': # if the user wants to add to the current directory
            PATH.append(t[1][1])
        elif t[1][0] == '-': # if the user wants to go down a directory(s)
            PATH.pop(len(t[1][1]))
