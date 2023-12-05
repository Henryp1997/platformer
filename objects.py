import pygame as pg
from variables import *

jumping = False
class player():
    def __init__(self):
        self.x = 100
        self.y = 500
        self.height = 30
        self.width = 30
        self.speed = 10
        self.rect = pg.Rect(self.x, self.y, self.width, self.height)
    def move(self):
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            self.rect.move_ip(self.speed,0)
            # self.x -= self.speed
        if key[pg.K_RIGHT]:
            self.rect.move_ip(self.speed,1)
            # self.x += self.speed
        self.draw_rect()
    def jump(self, platform_obj):
        key = pg.key.get_pressed()
        start_jump = False
        if key[pg.K_SPACE]:
            on_platform = self.check_collisions(platform_obj)
            if on_platform:
                start_jump = True
        
        original_y = self.y
        negate_speed = 1
        if start_jump:
            self.y -= negate_speed * 10
            if self.y < original_y - 50:
                negate_speed = -1
            on_platform = self.check_collisions(platform_obj)
            if on_platform:
                start_jump = False
            self.draw_rect()
        
    def check_collisions(self,platform_obj):
        on_platform = False
        if pg.Rect(self.x, self.y, self.width, self.height).colliderect(pg.Rect(platform_obj.x, platform_obj.y, platform_obj.width, platform_obj.height)):
            print("yes")
        if (self.y + self.height == platform_obj.y) and (platform_obj.x <= self.x + self.width and self.x <= platform_obj.x + platform_obj.width):
            on_platform = True
        if round(self.y + self.height) > screen_y - 10:
            on_platform = True
        if not on_platform:
            self.y += 10
        return on_platform


    
    def draw_rect(self):
        pg.draw.rect(screen, colours['RED'], pg.Rect((self.x, self.y), (self.width, self.height)))

class platform():
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw_rect(self):
        pg.draw.rect(screen, colours['BLUE'], pg.Rect((self.x, self.y), (self.width, self.height)))