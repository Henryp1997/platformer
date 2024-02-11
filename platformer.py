import pygame as pg
from pygame.locals import *
import sys
from variables import *
from objects import *

player = movable_character()
all_platforms = [platform(80, 350, 100, 20), platform(200, 350, 100, 20), platform(337, 550, 100, 20)]
frame_count = 0
frame_counts = [0, 60]
jumping = False

def main():
    # game code
    frame_count = 0
    frames = [0, 0]
    while True:
        clock = pg.time.Clock()
        clock.tick(60)
        screen.fill(colours['BLACK'])
        pg.draw.rect(screen, colours['GREY1'], pg.Rect((0,0), (screen_x, screen_y)), width=5)

        for platform_obj in all_platforms:
            platform_obj.draw_rect()

        player.move()
        player.move_up_down(frames)
        player.check_platform_collide(all_platforms)

        # only check jumps if player is on the ground
        # if player.on_ground:
        #     player.jump()

        # print(player_.state)

        # player_.check_collisions(platform_)
        # player_.jump(platform_) 

        pg.display.update()

        # update value of last frame so can keep track of time
        frame_count += 1
        frames[1] = frame_count

        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()

main()