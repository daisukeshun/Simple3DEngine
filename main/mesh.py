import pygame
from mymath import *

WHITE = (255, 255, 255)
class Triangle3D:
    def __init__(self, p1, p2, p3, width, height, focal_length):
        self.points = [0, 0, 0]
        self.points[0] = TranslateTo2D(p1, width, height, focal_length)
        self.points[1] = TranslateTo2D(p2, width, height, focal_length)
        self.points[2] = TranslateTo2D(p3, width, height, focal_length)
        # print(self.points)
    def draw3D(self, graphic):
        p = self.points
        pygame.draw.line(graphic, WHITE, p[0], p[1])
        pygame.draw.line(graphic, WHITE, p[1], p[2])
        pygame.draw.line(graphic, WHITE, p[2], p[0])

class Square3D:
    def __init__(self, p1, p2, p3, p4, width, height, focal_length):
        self.points = [0, 0, 0, 0]
        print(self.points)
        self.points[0] = TranslateTo2D(p1, width, height, focal_length)
        self.points[1] = TranslateTo2D(p2, width, height, focal_length)
        self.points[2] = TranslateTo2D(p3, width, height, focal_length)
        self.points[3] = TranslateTo2D(p4, width, height, focal_length)

    def draw3D(self, graphic):
        p = self.points
        pygame.draw.line(graphic, WHITE, p[0], p[1])
        pygame.draw.line(graphic, WHITE, p[1], p[2])
        pygame.draw.line(graphic, WHITE, p[2], p[3])
        pygame.draw.line(graphic, WHITE, p[3], p[0])

class mesh:
    def __init__(self, string):
        self.points = vertexLoad(string)
        self.faces = faceLoad(string)

    def meshDraw(self, window, width, height, focal_length, angle):
        m = self

        for i in m.faces:
            if (len(i) == 3):
                # Поиск точек
                p1 = m.points[i[0]-1]
                p2 = m.points[i[1]-1]
                p3 = m.points[i[2]-1]
                
                 # Умножение на матрицу поворота    
                p1 = rotateX(angle, p1)
                p2 = rotateX(angle, p2)
                p3 = rotateX(angle, p3)

                p1 = rotateY(angle, p1)
                p2 = rotateY(angle, p2)
                p3 = rotateY(angle, p3)

                v1 = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]
                v2 = [p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]]
                n  = crossProd(v1, v2)
                if (n[2] < 0):
                    tr = Triangle3D(p1, p2, p3, width, height, focal_length)
                    tr.draw3D(window)
                
            elif(len(i) == 4):
                p1 = m.points[i[0]-1]
                p2 = m.points[i[1]-1]
                p3 = m.points[i[2]-1]
                p4 = m.points[i[3]-1]
                
            
                p1 = rotateX(angle, p1)
                p2 = rotateX(angle, p2)
                p3 = rotateX(angle, p3)
                p4 = rotateX(angle, p4) 

                p1 = rotateY(angle, p1)
                p2 = rotateY(angle, p2)
                p3 = rotateY(angle, p3)
                p4 = rotateY(angle, p4)

                v1 = [p2[0] - p1[0], p2[1] - p1[1], p2[2] - p1[2]]
                v2 = [p3[0] - p1[0], p3[1] - p1[1], p3[2] - p1[2]]
                n = crossProd(v1, v2)
                if (n[2] < 0):
                    sq = Square3D(p1, p2, p3, p4, width, height, focal_length)
                    sq.draw3D(window)        

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
