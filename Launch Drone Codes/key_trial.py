#import cv2

class _Getch:
    """Gets a single character from standard input.  Does not echo to the
screen."""
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(3)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()




def get():
        getch = _Getch()
        while(1):
            k=getch()
            #print(k)
            if k!='':break
        if k =='\x1b[A':
                print "up"
        elif k=='\x1b[B':
                print "down"
        elif k=='\x1b[C':
                print "right"
        elif k=='\x1b[D':
                print "left"
        else:
             print(k)
                
                
def main():
        for i in range(0,10):
            get()

if __name__=='__main__':
        main()
                


