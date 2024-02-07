import pygame as pg
from variables import *

jumping = False
class player():
    def __init__(self):
        self.x = 100
        self.y = 200
        # self.height = 30
        # self.width = 30
        self.width = 32
        self.height = 64
        self.speed = 6
        self.yspeed = 5
        self.state = 0 # 0 = falling, 1 = on platform, 2 = jumping
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
        self.image = pg.image.load(f'{assets_path}/manic_miner.png').convert_alpha()

    def check_platform_collide(self, all_platforms):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.rect.move_ip(self.speed, 0)
            self.x -= self.speed
        if key[pg.K_RIGHT]:
            self.rect.move_ip(self.speed, 1)
            self.x += self.speed

        not_on_count = 0
        for platform_obj in all_platforms:
            player_below_platform = self.y + self.height > platform_obj.y
            player_about_to_land = self.y + self.height + self.yspeed >= platform_obj.y
            player_at_right_edge = self.x > platform_obj.x + platform_obj.width
            player_at_left_edge = self.x + self.width < platform_obj.x

            # start falling if not on platform
            if player_at_right_edge or player_at_left_edge:
                not_on_count += 1

            # player on platform
            if self.yspeed == 0:
                # snap player to platform
                self.y = platform_obj.y - self.height
            
            if player_about_to_land and not player_below_platform:
                # if the player is going to be inside the platform on the next frame
                self.yspeed = 0

        if not_on_count == len(all_platforms):
            self.yspeed = 5
    
        self.y += self.yspeed

        self.draw_rect()

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
        
    # def check_collisions(self, platform_obj):
        # on_platform = False
        # if pg.Rect(self.x, self.y, self.width, self.height).colliderect(pg.Rect(platform_obj.x, platform_obj.y, platform_obj.width, platform_obj.height)):
        #     print("yes")
        # if (self.y + self.height == platform_obj.y) and (platform_obj.x <= self.x + self.width and self.x <= platform_obj.x + platform_obj.width):
        #     on_platform = True
        # if round(self.y + self.height) > screen_y - 10:
        #     on_platform = True
        # if not on_platform:
        #     self.y += 10
        # return on_platform


        # check whether the player is going to be inside the platform on the next frame. If so, register a collision


    
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