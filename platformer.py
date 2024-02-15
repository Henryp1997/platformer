import pygame as pg
from pygame.locals import *
import sys
from variables import *
from objects import *

player = movable_character()
# all_platforms = [platform(5, 350, 840, 20), platform(337, 550, 100, 20)]
frame_count = 0
frame_counts = [0, 60]
jumping = False

def grid_platform(x, y, length, height):
    if x > 47 or y > 35 or x + length > 48 or y + height > 36:
        print("platform out of bounds")
        sys.exit()
    return platform(5 + (x * 20), 5 + (y * 20), length * 20, height * 20)

all_platforms = [
    grid_platform(0, 35, 48, 1),
    grid_platform(5, 15, 10, 1),
    grid_platform(20, 10, 10, 1),
    grid_platform(20, 25, 10, 1),
    grid_platform(30, 30, 5, 1),
    grid_platform(40, 22, 7, 1),
    grid_platform(25, 17, 15, 1),
    grid_platform(7, 5, 3, 1)
]
# all_platforms = [grid_platform(0, 35, 48, 1), grid_platform(20, 25, 10, 1)]

def main():
    # game code
    while True:
        clock = pg.time.Clock()
        clock.tick(60)
        screen.fill(colours['BLACK'])
        pg.draw.rect(screen, colours['GREY1'], pg.Rect((0,0), (screen_x, screen_y)), width=5)

        for platform_obj in all_platforms:
            platform_obj.draw_rect()

        player.move()
        player.move_up_down()
        player.check_wall_collide()
        player.check_platform_collide(all_platforms)
        player.jump()
        player.draw_rect()

        pg.display.update()

        # update value of last frame so can keep track of time
        player.update_time()

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

main()