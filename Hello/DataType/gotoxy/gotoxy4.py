from ctypes import *

def gotoxy(x,y):
    class COORD(Structure):
        pass
    COORD._fields_ = [("X", c_short), ("Y", c_short)]
    windll.kernel32.SetConsoleCursorPosition(windll.kernel32.GetStdHandle(-11), COORD(x,y))

gotoxy(40,10)
print("한사람")