# primitive repl-like dialog # nis 2018 January 05

# developed on Gemma M0 - likely to work on all CircuitPython hardware

# SEE ALSO
#   https://github.com/CharleyShattuck/Feather-M0-interpreter/blob/master/Interpreter.ino

# end of rollback series -- once again current.

# - - - - - - - - - - - - - - - - -

# limit - an int must be
# 0x3fffffff # 1073741823 # but not
# 0x40000000 - overflow (this is considered a long int)

# So this is a 30-bit unsigned value
# let's see what the signed limit is

# -1073741824 is the limit, as expected.

# 0x3f ff ff ff

# 1 1  3

import builtins ; import time

print("BEGIN.", end='')
print("the monotonic is: ", end='')

# time.monotonic() is good for 2^22 milliseconds (1.165 hours of wall-clock time)
# it is derated gracefully from there, by fewer updates without lost (millisecond-length) ticks

print(time.monotonic()) # seemed necessary when in a running program
# time.monotonic() # compiles but has no effects seen - REPL only, maybe.

versionne = "seven foxtrot three eff"

def prompt():
    print(" ok  ", end='',)
    print("the monotonic is: ", end='')
    print(time.monotonic(), end='')
    print(" ", end='')

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
    print(versionne, end=' ')
    print("OK. ", end='')

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
looping()
# looping()  # run this in the REPL:
#     'import main;main.looping()'
# END.
