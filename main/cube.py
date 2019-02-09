from graphics import *
from mymath import *
from mesh import *
from math import *

W = 600
H = 600
focal_length = 90

def main():
    win = GraphWin("Graph window", W, H)

    a = mesh('Cube/Cube.obj')
    a.undrawMesh(win)
    a.meshDraw(win, W, H, focal_length)

    pp = Point3D(0,0,0)
    print(pp.coords)

    pp = TranslateTo2D(pp.coords, W, H, 100)

    Ox = Triangle3D([1, 0, 0], [1, 0, 0], [0, 0, 0], W, H, 100)
    Oy = Triangle3D([0, 1, 0], [0, 1, 0], [0, 0, 0], W, H, 100)
    Oz = Triangle3D([0, 0, 1], [0, 0, 1], [0, 0, 0], W, H, 100)


    Oy.draw3D(win)
    Oy.drawPoints(win)
    Oz.draw3D(win)
    Oz.drawPoints(win)
    Ox.draw3D(win)
    Ox.drawPoints(win)
    pp.draw(win)
    win.getMouse()
    win.close()

main()





