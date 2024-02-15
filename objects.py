import pygame as pg
from variables import *

class movable_character():
    def __init__(self):
        self.x = 100
        self.y = 641
        # self.height = 30
        # self.width = 30
        self.width = 32
        self.height = 64
        self.speed = 6
        self.yspeed = 5
        self.yaccel = 0
        self.speeds = [5, 0, -5]
        self.accels = [0.2, 0, -0.2]

        # 0 = falling, 1 = on ground, 2 = jumping
        self.state = 1

        self.time = [0, 0]

        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.image = pg.image.load(f'{assets_path}/manic_miner.png').convert_alpha()

    def move(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.rect.move_ip(self.speed, 0)
            self.x -= self.speed
        if key[pg.K_RIGHT]:
            self.rect.move_ip(self.speed, 1)
            self.x += self.speed
    
    def jump(self):
        if self.state == 1: # on platform
            key = pg.key.get_pressed()
            if key[pg.K_SPACE]:
                self.jumped_pos = self.y
                self.state = 2
        elif self.state == 2: # currently jumping
            if self.y < self.jumped_pos - self.height*2:
                self.state = 0
                self.jumped_pos = 0
                self.time = [0, 0]

    def check_wall_collide(self):
        hit_right_wall = self.x + self.width >= screen_x - 5
        if hit_right_wall:
            self.x = screen_x - 5 - self.width
            return
        hit_left_wall = self.x <= 5
        if hit_left_wall:
            self.x = 5
            return

    def check_platform_collide(self, all_platforms):
        not_on_count = 0
        for platform_obj in all_platforms:     
             
            # start falling if not on platform. Check individually for performance
            player_at_right_edge = self.x > platform_obj.x + platform_obj.width
            if player_at_right_edge:
                not_on_count += 1
                continue

            player_at_left_edge = self.x + self.width < platform_obj.x
            if player_at_left_edge:
                not_on_count += 1
                continue
                
            player_below_platform = self.y + self.height > platform_obj.y
            if player_below_platform:
                not_on_count += 1
                continue

            player_about_to_land = self.y + self.height + self.yspeed >= platform_obj.y
            if not player_about_to_land:
                not_on_count += 1
                continue

            # if player is about to land on the current platform
            if player_about_to_land and not player_below_platform:
                # snap player to platform
                self.y = platform_obj.y - self.height
                self.state = 1
                break

        if not_on_count == len(all_platforms) and self.state != 2:
            self.state = 0

        return

    # def move_up_down(self):
    #     time_passed = self.time[1] - self.time[0]
    #     self.yaccel = self.accels[self.state]
    #     self.yspeed = time_passed * self.yaccel
    #     self.y += self.yspeed

    def move_up_down(self):
        self.yspeed = self.speeds[self.state]
        self.y += self.yspeed

    # def jump(self, platform_obj):
    #     key = pg.key.get_pressed()
    #     start_jump = False
    #     if key[pg.K_SPACE]:
    #         on_platform = self.check_collisions(platform_obj)
    #         if on_platform:
    #             start_jump = True
        
    #     original_y = self.y
    #     negate_speed = 1
    #     if start_jump:
    #         self.y -= negate_speed * 10
    #         if self.y < original_y - 50:
    #             negate_speed = -1
    #         on_platform = self.check_collisions(platform_obj)
    #         if on_platform:
    #             start_jump = False
    #         self.draw_rect()
    
    def update_time(self):
        self.time[1] += 1
        if self.state == 1:
            # reset time calculations if not falling or jumping
            self.time = [0, 0]

    def draw_rect(self):
        # pg.draw.rect(screen, colours['RED'], pg.Rect((self.x, self.y), (self.width, self.height)))
        screen.blit(self.image, (self.x, self.y))

class platform():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw_rect(self):
        pg.draw.rect(screen, colours['BLUE'], pg.Rect((self.x, self.y), (self.width, self.height)))