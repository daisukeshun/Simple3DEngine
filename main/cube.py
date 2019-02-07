from graphics import *
from mymath import *
from mesh import *
from math import *

W = 600
H = 600
focal_length = 100

def main():
    win = GraphWin("Graph window", W, H)

    a = mesh('cube/Cube.obj')
    a.undrawMesh(win)
    a.meshDraw(win, W, H, focal_length)

    pp = Point(0.001*focal_length/0.5+W/2, 0.001*focal_length/0.5+H/2)
    pp.draw(win)
    win.getMouse()
    win.close()

main()





