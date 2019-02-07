from graphics import *
from mymath import *

class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

class mesh:
    def __init__(self, string):
        self.points = vertexLoad(string)
        self.faces = faceLoad(string)


def vertexLoad(string):
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


def faceLoad(string):
    f = open(string)
    faces = []
    for x in f:
        if (x[0] == 'f'):
            a = x.split()
            a.remove('f')
            for i in range(len(a)):
                a[i] = int((a[i][:a[i].index('/')]))
            faces.append(a)
    return faces

W = 600
H = 600

def main():
    win = GraphWin("Graph window", W, H)

    a1 = Point3D(0, 0, 1)
    a2 = Point3D(0, 1, 1)
    a3 = Point3D(1, 1, 1)

    b = Triangle3D(a1, a2, a3, 100, W, H)
    b.draw3D(win)

    win.getMouse()
    win.close()
    print(win.winfo_width)

# main()


m = mesh('45-trees/tree01.obj')
print(m.points)
print('\n\n\n')
print(m.faces)