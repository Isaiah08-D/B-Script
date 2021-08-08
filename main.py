from vars import Vars
from compile import Compile

vars = Vars()
compile = Compile()

while True:
    code = input('>>> ')
    t = compile.compile(vars, code)
    if t[0] == 'ERROR':
        print(t[0] + '\n' + t[1])
    elif t[0] == 'END':
        print('END')
        break
    elif t[0] == 'VAR':
        if t[1][0] == 'def': # if the user is defining a new function or changing a variable completely
            vars.add(t[1][1], t[1][2])



