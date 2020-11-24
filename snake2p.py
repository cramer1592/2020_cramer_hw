import pygame as pg
import random
from pg.constants import *

pg.init()

#COLORLIST
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
GREEN = (0, 255, 0)
BLUE = (0, 0 , 255)

#PARAMETERS
aspect_ratio = (800, 600)

class Player:
    x_pos = 0
    y_pos = 0
    dx_pos = 0
    dy_pos = 0

    def __init__(self, display):
        self.display = display
    
    def keystroke(self, event):
        if event.type == KEYDOWN:
            if evennt.key == K_LEFT:
                self.dx_git pos = -10
                self.dy_pos = 0
            elif evennt.key == K_RIGHT:
                self.dx_pos = 10
                self.dy_pos = 0
            elif evennt.key == K_UP:
                self.dx_pos = 0
                self.dy_pos = -10
            elif evennt.key == K_DOWN:
                self.dx_pos = 0
                self.dy_pos = 10

    def locomotion(self):
        self.x_pos += self.dx_pos
        self.y_pos += self.dy_pos

class Food:


f_c = []
for _ in range(5):
    f_x = random.randint(0, 79)
    f_y = random.randint(0, 59)
    f_c.append((10*f_x, 10*f_y))
f_a = [True for _ in range(5)]

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption('HW3 Snake Game')
game_display.fill(BLACK)
pygame.draw.rect(game_display, WHITE, [x, y, 10, 10])
pygame.display.update()
clock = pygame.time.Clock()

class Player:
    x = 0
    y = 0
    dx = 0
    dy = 0

class Food:
    x = 0
    y = 0
    active = True
    def __init__(self):
        self.x = random.randint(0, 79)
        self.y = random.randint(0, 59)

game_over = False

pl_1 = Player()
fds = [Food() for _ in range(20)]

while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True
            break
        elif event.type == KEYDOWN:
            if event.key == K_LEFT:
                dx = -10
                dy = 0
            elif event.key == K_RIGHT:
                dx = 10
                dy = 0
            elif event.key == K_UP:
                dx = 0
                dy = -10
            elif event.key == K_DOWN:
                dx = 0
                dy = 10
                
    pl_1.x += pl_1.dx
    pl_1.y += pl_2.dy
    game_display.fill(BLACK)
    pygame.draw.rect(game_display, WHITE, [x, y, 10, 10])
    for i, (f_x, f_y) in enumerate(f_c):
        if f_a[i] == True:
            pygame.draw.rect(game_display, GREEN, [f_x, f_y, 10, 10])
    for i, (f_x, f_y) in enumerate(f_c):
        if x == f_x and y == f_y:
            f_a[i] = False
            pygame.draw.rect(game_display, RED, [f_x, f_y, 10, 10])
    
    f_r =  False
    for active in f_a:
        if active:
            f_r = True
        else:
            pass

    if not f_r:
        game_over = True

    pygame.display.update()
    clock.tick(12)
