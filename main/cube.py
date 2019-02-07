from graphics import *
from mymath import *
from mesh import *
from math import *

W = 1000
H = 600
focal_length = 100

def main():
    win = GraphWin("Graph window", W, H)

    a = mesh('cube/Cube.obj')
    a.undrawMesh(win)
    a.meshDraw(win, W, H, focal_length)

    win.getMouse()
    win.close()

main()





