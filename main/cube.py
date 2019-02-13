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
    c = mesh('tree02.obj')
    d = mesh('tree03.obj')
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
        if mouse_mv:
                angle[1] += mouse_mv[0]*0.5
                angle[0] += mouse_mv[1]*0.5


        if keys_pressed[pygame.K_w]:
                Camera[2] -= 0.2
        if keys_pressed[pygame.K_s]:
                Camera[2] += 0.2
        if keys_pressed[pygame.K_a]:
                Camera[0] += 0.2
        if keys_pressed[pygame.K_d]:
                Camera[0] -= 0.2
        if keys_pressed[pygame.K_LEFT]:
                angle[1] -= 4
        if keys_pressed[pygame.K_RIGHT]:
                angle[1] += 4
        if keys_pressed[pygame.K_UP]:
                angle[0] -= 4
        if keys_pressed[pygame.K_DOWN]:
                angle[0] += 4

        pygame.draw.rect(win, BLACK, (0,0, W, H))
        b.meshDraw(win, W, H, focal_length, angle, Camera)
        a.meshDraw(win, W, H, focal_length, angle, Camera)
        c.meshDraw(win, W, H, focal_length, angle, Camera)
        d.meshDraw(win, W, H, focal_length, angle, Camera)
        pygame.display.update()
main()





