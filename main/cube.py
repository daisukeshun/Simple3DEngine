from graphics import *
from mymath import *
from mesh import *
from math import *

W = 600
H = 600
focal_length = 100

def main():
    win = GraphWin("Graph window", W, H)

    # ss = Square3D([100, 200, 2], [100, 100, 2], [200, 100, 2],
    #               [200, 200, 2],  300, 200, 1000, 0.1)

    # ss = TranslateTo2D(ss, 90, W, H, 1000, 0.1)
    # ss.draw3D(win)
    win.getMouse()
    win.close()

main()





