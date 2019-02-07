from graphics import *
from mymath import *
from mesh import *
from math import *

W = 1200
H = 600
Fov = 100
viewLen = 1000

def main():
    # win = GraphWin("Graph window", W, H)
    m = mesh('45-trees/tree01.obj')

    for i in range(len(m.faces)):
        print(len(m.faces[i]))
        if (len(m.faces[i]) == 4):
            for j in range(len(m.faces)):
                print(m.faces[j], m.faces[j])
                print(m.points[m.faces[j][0]-1])
                print(m.points[m.faces[j][1]-1])
                print(m.points[m.faces[j][2]-1])
                print(m.points[m.faces[j][3]-1])
                # a = Square3D(p1, p2, p3, p4, Fov, W, H, viewLen)
                # a.draw3D(win)
        elif(len(m.faces[i] == 3)):
            print(m.points[m.faces[j][0]-1])
            print(m.points[m.faces[j][1]-1])
            print(m.points[m.faces[j][2]-1])

        else:
            print(len(m.faces[i]))
            # b = Triangle3D(p1, p2, p3, Fov, W, H, viewLen)
            # b.draw3D(win)


    # win.getMouse()
    # win.close()
    # print(win.winfo_width)

# main()


m = mesh('45-trees/tree01.obj')
for i in m.faces:
    if (len(i) == 3):
        print(m.points[i[0]], m.points[i[1]], m.points[i[2]])
    elif(len(i) == 4):
        print(m.points[i[0]], m.points[i[1]], m.points[i[2]], m.points[i[3]])


# m = mesh('45-trees/tree01.obj')
# print(m.points)
# print('\n\n\n')
# print(m.faces)

# print(tan(radians(45)))
