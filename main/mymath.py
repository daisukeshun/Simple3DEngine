import pygame
from math import *

def mmult(i, m):
    o = []
    if len(m) == 3:
        o.append(i[0] * m[0][0] + i[1]*m[1][0] + i[2]*m[2][0])
        o.append(i[0] * m[0][1] + i[1]*m[1][1] + i[2]*m[2][1])
        o.append(i[0] * m[0][2] + i[1]*m[1][2] + i[2]*m[2][2])
    elif len(m) == 4:
        o.append(i[0] * m[0][0] + i[1]*m[1][0] + i[2]*m[2][0] + i[3]*m[3][0])
        o.append(i[0] * m[0][1] + i[1]*m[1][1] + i[2]*m[2][1] + i[3]*m[3][0])
        o.append(i[0] * m[0][2] + i[1]*m[1][2] + i[2]*m[2][2] + i[3]*m[3][0])
        o.append(i[0] * m[0][2] + i[1]*m[1][2] + i[2]*m[2][2] + i[3]*m[3][0])
    return o

def TranslateTo2D(Point3, width, height, focal_length, camera):
    zFar = 1000
    zNear = 0.1
    w = Point3[2] + camera[2]
    _x = (Point3[0] + camera[0])* width/2
    _y = -(Point3[1] + camera[1])* width/height * height/2
    _z = Point3[2] * (zFar/(zFar - zNear)) - zFar*zNear/(zFar - zNear) + camera[2]
    if w > 0:
        _x /= w
        _y /= w
        _z /= w

    _x += width/2
    _y += height/2
    a = [_x, _y]
    return a

def rotateX(angle, point):
    angle = radians(angle)
    m = [[1, 0, 0],
        [0, cos(angle), -sin(angle)],
        [0, sin(angle), cos(angle)]]    
    res = mmult(point, m)
    return res


def rotateY(angle, point):
    angle = radians(angle)
    m = [[cos(angle), 0, sin(angle)],
         [0, 1, 0],
         [-sin(angle), 0, cos(angle)]]
    res = mmult(point, m)
    return res

def rotateZ(angle, point):
    angle = radians(angle)	
    m = [[cos(angle), -sin(angle), 0 ],
         [sin(angle), cos(angle), 0 ],
         [0, 0, 1]];
    res = mmult(point, m)
    return res

def dotProduct(v1, v2):
    return v1[0]*v2[0] + v1[1]*v2[1] + v1[2]*v2[2]

def crossProd(v1, v2):
    res = [
        v1[1] * v2[2] - v1[2] * v2[1],
        v1[2] * v2[0] - v1[0] * v2[2],
        v1[0] * v2[1] - v1[1] * v2[0]
    ]
    return res
