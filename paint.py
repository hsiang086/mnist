import pygame
from math import cos, sin
import cv2
import numpy as np

def init():
    global BLACK, WHITE
    global FPS
    global RES, W, H
    global paint_board
    global pixel_w, pixel_h
    global screen
    global clock
    global r
    global img
    BLACK, WHITE = (0, 0, 0), (255, 255, 255)
    FPS = 240
    RES = W, H = 280, 280
    paint_board = (280, 280)
    pixel_w, pixel_h = W / paint_board[0], H / paint_board[1]
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((RES))
    screen.fill(WHITE)
    r = 10
    img = np.ones((paint_board[0], paint_board[1])) * 255

init()
while True:
    clock.tick(FPS)
    pygame.display.set_caption("FPS: {:.2f}".format(clock.get_fps()))
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        pos_x = int(mouse_pos[0] // pixel_w)
        pos_y = int(mouse_pos[1] // pixel_h)
        for theta in range(628):
            for R in range(r):
                x = int(R * cos(theta / 100) + pos_x)
                y = int(R * sin(theta / 100) + pos_y)
                if x < paint_board[0] and y < paint_board[1]:
                    img[x][y] = 0
    for i in range(paint_board[0]):
        for j in range(paint_board[1]):
            if img[i][j] != 255:
                color = (int(img[i][j]), int(img[i][j]), int(img[i][j]))
                paint = pygame.Rect((i * pixel_w, j * pixel_h), (pixel_w, pixel_h))
                pygame.draw.rect(screen, color, paint)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                screen.fill(WHITE)
                img = np.ones((paint_board[0], paint_board[1])) * 255
            if event.key == pygame.K_s:
                img_saved = cv2.resize(img, (28, 28))
                np.save("img", img_saved)
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
