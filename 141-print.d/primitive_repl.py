# primitive repl-like dialog # nis 2018 January 05

# developed on Gemma M0 - likely to work on all CircuitPython hardware

import builtins
import time
counter = 4

# ---------------------------
print("turna sevixale bce78")
# ---------------------------

# ----------------- granular

# -----------------fuzzy

def ESC_color():
    print("\x1b\x5b0;1;", end='',)

def neutral():
    ESC_color()
    print("0m", end='',)

# -----------------fuzzy

def prompt():
    print(" ok", end='',)

def get_things():
    # Value=input("Please type a value:")
    # Value=raw_input()
    Value=input(self)
    print(Value)
    print()
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
