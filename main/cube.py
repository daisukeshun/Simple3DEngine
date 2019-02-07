from graphics import *
from mymath import *

class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

class Triangle3D:
    def __init__(self, p1, p2, p3, focal_length, width, height):
        self.points = []
        self.points[0] = TranslateTo2D(p1, focal_length, width, height)
        self.points[1] = TranslateTo2D(p2, focal_length, width, height)
        self.points[2] = TranslateTo2D(p3, focal_length, width, height)
        print('\n\n\n\n\n')
        print(self.points)
        print('\n\n\n\n\n')


    def draw3D(self, graphic):
        p = self.points
        Line(p[0], p[1]).draw(graphic)
        Line(p[1], p[2]).draw(graphic)
        Line(p[2], p[0]).draw(graphic)


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

# main()



v = meshLoad('45-trees/tree01.obj')
print(v)
