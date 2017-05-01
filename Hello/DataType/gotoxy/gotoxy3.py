from ctypes import *

def print_at(r, c, s):
    STD_OUTPUT_HANDLE = -11
    class COORD(Structure):
        pass
    COORD._fields_ = [("X", c_short), ("Y", c_short)]
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(c, r))
    s=s.encode("windows-1252")
    windll.kernel32.WriteConsoleA(h, c_char_p(s), len(s), None, None)


print_at(6, 30, "hello")