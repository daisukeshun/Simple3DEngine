from graphics import *

class Point3D:
    def __init__(self, x, y, z):
        self.x = x/1
        self.y = y/1
        self.z = z/1



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
