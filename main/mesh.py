from graphics import *
from mymath import *


class mesh:
    def __init__(self, string):
        self.points = vertexLoad(string)
        self.faces = faceLoad(string)

    def meshDraw(self, window, width, height, focal_length):
        m = self
        v1 = [0,0,0]
        v2 = [0,0,0]
        n  = [0,0,0]

        for i in m.faces:
            if (len(i) == 3):
                p1 = m.points[i[0]-1]
                p2 = m.points[i[1]-1]
                p3 = m.points[i[2]-1]
                
                
                v1[0] = p2[0] - p1[0] 
                v1[1] = p2[1] - p1[1]
                v1[2] = p2[2] - p1[2]

                v2[0] = p3[0] - p1[0]
                v2[1] = p3[1] - p1[1]
                v2[2] = p3[2] - p1[2]

                n[0] = v1[1] * v2[2] - v1[2] * v2[1]
                n[1] = v1[2] * v2[0] - v1[0] * v2[2]
                n[2] = v1[0] * v2[1] - v1[1] * v2[0]

                # if(n[0] * p1[0] - Camera[0] + n[1] * p1[1] - Camera[1] + n[2] * p1[2] - Camera[2] < 0 and n[2] < 0):
                # if(n[2] < 0):

                # tr = Triangle3D(p1, p2, p3, width, height, focal_length)
                # tr.draw3D(window)
                # tr.drawPoints(window)
                
                
            elif(len(i) == 4):
                p1 = m.points[i[0]-1]
                p2 = m.points[i[1]-1]
                p3 = m.points[i[2]-1]
                p4 = m.points[i[3]-1]

                p1[2] += 1
                p2[2] += 1
                p3[2] += 1
                p4[2] += 1

                # p1 = RotateX(20, p1)  # 90 270
                # p1 = RotateX(20, p1)  # 90 270
                # p1 = RotateX(20, p1)  # 90 270
                # p1 = RotateX(20, p1)  # 90 270


                v1[0] = p2[0] - p1[0]
                v1[1] = p2[1] - p1[1]
                v1[2] = p2[2] - p1[2]

                v2[0] = p3[0] - p1[0]
                v2[1] = p3[1] - p1[1]
                v2[2] = p3[2] - p1[2]

                n[0] = v1[1] * v2[2] - v1[2] * v2[1]
                n[1] = v1[2] * v2[0] - v1[0] * v2[2]
                n[2] = v1[0] * v2[1] - v1[1] * v2[0]

                # if(n[0] * p1[0] - Camera[0] + n[1] * p1[1] - Camera[1] + n[2] * p1[2] - Camera[2] < 0 and n[2] < 0):
                # if(n[2] < 0):
                # sq = Square3D(p1, p2, p3, p4, width, height, focal_length)
                # sq.draw3D(window)
                # sq.drawPoints(window)
                
            

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

