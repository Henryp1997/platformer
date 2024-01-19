import pygame as pg
from pygame.locals import *
import sys
from variables import *
from objects import *

player_ = player()
all_platforms = [platform(80, 350, 100, 20), platform(200, 350, 100, 20), platform(340, 350, 100, 20)]
frame_count = 0
frame_counts = [0, 60]
jumping = False

def main():
    # game code
    while True:
        clock = pg.time.Clock()
        clock.tick(60)
        screen.fill(colours['BLACK'])
        pg.draw.rect(screen, colours['GREY1'], pg.Rect((0,0), (screen_x, screen_y)), width=5)

        for platform_obj in all_platforms:
            platform_obj.draw_rect()
        player_.check_platform_collide(all_platforms)
        # print(player_.state)

        # player_.check_collisions(platform_)
        # player_.jump(platform_) 

        pg.display.update()
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

main()