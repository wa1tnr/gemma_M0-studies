# primitive repl-like dialog # nis 2018 January 05

# developed on Gemma M0 - likely to work on all CircuitPython hardware

# SEE ALSO
#   https://github.com/CharleyShattuck/Feather-M0-interpreter/blob/master/Interpreter.ino

# rollback -- establishing the history of this file (all 36 hours of it).

import builtins
import time
counter = 4

# ---------------------------
print("turna sevixale bce78")
# ---------------------------

def ESC_color():
    print("\x1b\x5b0;1;", end='',)

def neutral():
    ESC_color()
    print("0m", end='',)

# -----------------fuzzy

def prompt():
    print(" ok", end='\n',)

    # print(" ok", end='\n',)

def get_things():
    # tib=input("prompted for tib content:")
    # tib=raw_input()
    tib=input()
    tab=int(tib)
    tab=tab - 11
    print(tab)
    prompt()

def signon():
    neutral(); print("OK. ", end='')
    time.sleep(0.28)

# ----------------              -----------------

def looping():
    while True:
        global counter
        get_things()
        counter = counter + 1
        time.sleep(0.28)

# - - - - - - - - - - - - - - - - - - - -
# Let's get going..

signon()
# looping()


# end of program.  See sample run, below:

# --- end of sample run ---
# END.
