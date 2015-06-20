import os

def clrscr():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
