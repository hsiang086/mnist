import pygame
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
    paint_board = (28, 28)
    pixel_w, pixel_h = W / paint_board[0], H / paint_board[1]
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((RES))
    screen.fill(WHITE)
    r = 9
    img = np.ones((paint_board[0], paint_board[1]))

init()
running = True
while running:
    clock.tick(FPS)
    pygame.display.set_caption("FPS: {:.2f}".format(clock.get_fps()))
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    if mouse_pressed[0]:
        x, y = int(mouse_pos[0] // pixel_w), int(mouse_pos[1] // pixel_h)
        img[x][y] = 0.0
        paint = pygame.Rect((x * pixel_w, y * pixel_h), (pixel_w, pixel_h))
        pygame.draw.rect(screen, BLACK, paint)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                screen.fill(WHITE)
                img = np.ones((paint_board[0], paint_board[1]))
            if event.key == pygame.K_s:
                img_saved = cv2.GaussianBlur(img, (3, 3), 0)
                np.save("img", img_saved)
                print("img saved")
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
pygame.quit()