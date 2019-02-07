from graphics import *
from mymath import *

class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

def meshLoad(string):
    vertices = []
    f = open(string)
    for x in f:
        if(x[0] == 'v' and x[1] != 'n'):
            a = x.split()
            a.remove('v')
            for i in range(len(a)):
                a[i] = float(a[i])
            vertices.append(a)
    return vertices


W = 600
H = 600

def main():
    win = GraphWin("Graph window", W, H)

    a1 = Point3D(10, 10, 10)
    a2 = Point3D(10, 20, 1)
    a3 = Point3D(20, 20, 1)

    b = Triangle3D(a1, a2, a3, 10, W, H)
    b.draw3D(win)

    win.getMouse()
    win.close()
    print(win.winfo_width)

main()