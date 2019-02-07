from graphics import *
from mymath import *

class Triangle3D:
    def __init__(self, p1, p2, p3, width, height, focal_length):
        self.points = [0, 0, 0]
        self.points[0] = TranslateTo2D(p1, focal_length, width, height)
        self.points[1] = TranslateTo2D(p2, focal_length, width, height)
        self.points[2] = TranslateTo2D(p3, focal_length, width, height)

    def draw3D(self, graphic):
        p = self.points
        Line(p[0], p[1]).draw(graphic)
        Line(p[1], p[2]).draw(graphic)
        Line(p[2], p[0]).draw(graphic)


class Square3D:
    def __init__(self, p1, p2, p3, p4, width, height, focal_length):
        self.points = [0, 0, 0, 0]
        self.points[0] = TranslateTo2D(p1, width, height, focal_length)
        self.points[1] = TranslateTo2D(p2, width, height, focal_length)
        self.points[2] = TranslateTo2D(p3, width, height, focal_length)
        self.points[3] = TranslateTo2D(p4, width, height, focal_length)

    def draw3D(self, graphic):
        p = self.points
        Line(p[0], p[1]).draw(graphic)
        Line(p[1], p[2]).draw(graphic)
        Line(p[2], p[3]).draw(graphic)
        Line(p[3], p[0]).draw(graphic)


class mesh:
    def __init__(self, string):
        self.points = vertexLoad(string)
        self.faces = faceLoad(string)

    def meshDraw(self, window, width, height, focal_length):
        m = self
        for i in m.faces:
            if (len(i) == 3):
                p1 = m.points[i[0]-1]
                p2 = m.points[i[1]-1]
                p3 = m.points[i[2]-1]
                tr = Triangle3D(p1, p2, p3, width, height, focal_length)
                tr.draw3D(window)
                # print(tr.points)
                # print(p1, p2, p3)
                
            elif(len(i) == 4):
                p1 = m.points[i[0]-1]
                p2 = m.points[i[1]-1]
                p3 = m.points[i[2]-1]
                p4 = m.points[i[3]-1]
                sq = Square3D(p1, p2, p3, p4, width, height, focal_length)
                sq.draw3D(window)
                # print(sq.points)
                # print(p1, p2, p3, p4)

    def undrawMesh(self, win):
        for item in win.items[:]:
            item.undraw()
        win.update()



def vertexLoad(string):
    vertices = []
    f = open(string)
    for x in f:
        if(x[0] == 'v' and x[1] != 'n' and x[1] != 't'):
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
