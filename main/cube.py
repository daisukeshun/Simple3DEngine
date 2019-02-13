import pygame
from pygame import *
from mymath import *
from mesh import *
from math import *



def main():
    W = 1200
    H = 600
    BLACK = (0, 0, 0)
    focal_length = 90
    pygame.init()
    win = pygame.display.set_mode((W, H))
    Camera = [0.0,0.0,0.0,0.0]

    a = mesh('tree01.obj')
    b = mesh('Cube.obj')
    clock = pygame.time.Clock()
    angle = [0,0,0]
    loop = True
    while loop:
        clock.tick(60)
        for i in pygame.event.get():
                if i.type == pygame.QUIT:
                        loop = False
                elif i.type == pygame.KEYDOWN and i.key == pygame.K_ESCAPE:
                        loop = False

        keys_pressed = pygame.key.get_pressed()
        mouse_mv = pygame.mouse.get_rel()
        # print(mouse_mv[0])

        # if mouse_mv:
        #         angle[0] += mouse_mv[0]*0.01
        #         Camera[0] += mouse_mv[0]*0.01
        #         angle[1] += mouse_mv[1]*0.01
        #         Camera[1] += mouse_mv[1]*0.01


        if keys_pressed[pygame.K_w]:
                Camera[2] -= 0.2
        if keys_pressed[pygame.K_s]:
                Camera[2] += 0.2
        if keys_pressed[pygame.K_a]:
                Camera[0] += 0.2
        if keys_pressed[pygame.K_d]:
                Camera[0] -= 0.2
        if keys_pressed[pygame.K_LEFT]:
                Camera[0] += 0.2
                angle[1] -= 3
        if keys_pressed[pygame.K_RIGHT]:
                Camera[0] -= 0.2
                angle[1] += 3
        if keys_pressed[pygame.K_UP]:
                Camera[1] -= 0.2
                angle[0] -= 3
        if keys_pressed[pygame.K_DOWN]:
                Camera[1] += 0.2
                angle[0] += 3

        pygame.draw.rect(win, BLACK, (0,0, W, H))
        b.meshDraw(win, W, H, focal_length, angle, Camera)
        a.meshDraw(win, W, H, focal_length, angle, Camera)
        # print(Camera)
        pygame.display.update()
main()





