# aprimitive repl-like dialog # nis 2018 January 05

# developed on Gemma M0 - likely to work on all CircuitPython hardware

# SEE ALSO
#   https://github.com/CharleyShattuck/Feather-M0-interpreter/blob/master/Interpreter.ino

# rollback -- establishing the history of this file (all 36 hours of it).

import builtins ; import time

def prompt():
    print(" ok  ", end='',)

def get_things():
    global tib ; tib=input(); # terminal input buffer
    global tab ; tab=''
    try:
        tab='' ; tab = int(tib)

    except ValueError:
        pass

    if (isinstance(tab, int)):
        print("tab was an int. ", end='')

    prompt() ; return tab, tib

def signon():
    print("ooask. ", end='')
    print("OK. ", end='')

# ----------------              -----------------

def looping():

    while True:
        get_things()
        if (isinstance(tab, int)):
            print("printing integer tab: ", end='')
            print(tab)
            print("less 7: ", end='')
            print(tab -7)

        if (isinstance(tab, str)):
            m = 1 ; # noop # print("ERROR - detect and ignore.")

        if (isinstance(tib, str)):
            if (len(tib) > 0):
                print("printing the str, tib, the terminal input buffer: ")
                print(tib)

        time.sleep(0.128)
# - - - - - - - - - - - - - - - - - - - -
signon()
# looping()  # run this in the REPL:
#     'import main;main.looping()'
# END.
