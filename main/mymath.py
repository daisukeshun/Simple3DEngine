from graphics import *

class Point3D:
    def __init__(self, x, y, z):
        self.x = x/1
        self.y = y/1
        self.z = z/1


class Triangle3D:
    def __init__(self, p1, p2, p3, focal_length, width, height):
        self.points = [0,0,0]
        self.points[0] = TranslateTo2D(p1, focal_length, width, height)
        self.points[1] = TranslateTo2D(p2, focal_length, width, height)
        self.points[2] = TranslateTo2D(p3, focal_length, width, height)

    def draw3D(self, graphic):
        p = self.points
        Line(p[0], p[1]).draw(graphic)
        Line(p[1], p[2]).draw(graphic)
        Line(p[2], p[0]).draw(graphic)


def TranslateTo2D(Point3D, focal_length, width, height):
        _x = Point3D.x*(focal_length/Point3D.z) + width/2 
        _y = Point3D.y*(focal_length/Point3D.z) + height/2
        _a = Point(_x, _y)
        return _a

def matmult(A, B):
    C = [[0 for row in range(len(A))] for col in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k]*B[k][j]
    return C
