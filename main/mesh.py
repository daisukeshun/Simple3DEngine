from graphics import *
from mymath import *

class Triangle3D:
    def __init__(self, p1, p2, p3, fov, width, height, viewLengh):
        self.points = [0, 0, 0]
        self.points[0] = TranslateTo2D(p1, fov, width, height, viewLengh)
        self.points[1] = TranslateTo2D(p2, fov, width, height, viewLengh)
        self.points[2] = TranslateTo2D(p3, fov, width, height, viewLengh)

    def draw3D(self, graphic):
        p = self.points
        Line(p[0], p[1]).draw(graphic)
        Line(p[1], p[2]).draw(graphic)
        Line(p[2], p[0]).draw(graphic)


class Square3D:
    def __init__(self, p1, p2, p3, p4, fov, width, height, viewLengh):
        self.points = [0, 0, 0, 0]
        self.points[0] = TranslateTo2D(p1, fov, width, height, viewLengh)
        self.points[1] = TranslateTo2D(p2, fov, width, height, viewLengh)
        self.points[2] = TranslateTo2D(p3, fov, width, height, viewLengh)
        self.points[3] = TranslateTo2D(p4, fov, width, height, viewLengh)

    def draw3D(self, graphic):
        p = self.points
        Line(p[0], p[1]).draw(graphic)
        Line(p[1], p[2]).draw(graphic)
        Line(p[2], p[3]).draw(graphic)
        Line(p[3], p[0]).draw(graphic)


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
