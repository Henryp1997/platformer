import pygame as pg
from pygame.locals import *
import sys
from variables import *
from objects import *

player_ = player()
platform_ = platform(80, 630, 100, 20)
frame_count = 0
frame_counts = [0,60]
jumping = False
# game code
while True:
    clock = pg.time.Clock()
    clock.tick(60)
    screen.fill(colours['BLACK'])
    pg.draw.rect(screen, colours['GREY1'], pg.Rect((0,0), (screen_x, screen_y)), width=5)
    player_.move()
    platform_.draw_rect()

    player_.check_collisions(platform_)
    player_.jump(platform_) 

    pg.display.update()
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
    frame_count += 1
    frame_counts[1] = frame_count
    