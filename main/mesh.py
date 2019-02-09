from graphics import *
from mymath import *

class Triangle3D:
    def __init__(self, p1, p2, p3, width, height, focal_length):
        self.points = [0, 0, 0]
        self.points[0] = TranslateTo2D(p1, width, height, focal_length)
        self.points[1] = TranslateTo2D(p2, width, height, focal_length)
        self.points[2] = TranslateTo2D(p3, width, height, focal_length)

    def draw3D(self, graphic):
        p = self.points
        Line(p[0], p[1]).draw(graphic)
        Line(p[1], p[2]).draw(graphic)
        Line(p[2], p[0]).draw(graphic)

    def drawPoints(self, graphic):
        p = self.points
        for i in p:
            i.draw(graphic)
            print('Triangle')

class Square3D:
    def __init__(self, p1, p2, p3, p4, width, height, focal_length):
        print(p1, p2, p3, p4)
        self.points = [0, 0, 0, 0]

        # p1[2] += 3
        # p2[2] += 3
        # p3[2] += 3
        # p4[2] += 3



        self.points[0] = TranslateTo2D(p1, width, height, focal_length)
        self.points[1] = TranslateTo2D(p2, width, height, focal_length)
        self.points[2] = TranslateTo2D(p3, width, height, focal_length)
        self.points[3] = TranslateTo2D(p4, width, height, focal_length)
        print(self.points)
    def draw3D(self, graphic):
        p = self.points
        Line(p[0], p[1]).draw(graphic)
        Line(p[1], p[2]).draw(graphic)
        Line(p[2], p[3]).draw(graphic)
        Line(p[3], p[0]).draw(graphic)


    def drawPoints(self, graphic):
        p = self.points
        for i in p:
            i.draw(graphic)

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
                # tr.drawPoints(window)
                tr.draw3D(window)
                
            elif(len(i) == 4):
                p1 = m.points[i[0]-1]
                p2 = m.points[i[1]-1]
                p3 = m.points[i[2]-1]
                p4 = m.points[i[3]-1]
                sq = Square3D(p1, p2, p3, p4, width, height, focal_length)
                # sq.drawPoints(window)
                sq.draw3D(window)
                print(i)

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
