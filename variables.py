import pygame as pg

colours = {
    'BLUE': (0, 100, 200),
    'DARK_BLUE': (0,55,255),
    'RED' : (225, 25, 25),
    'YELLOW': (255, 255, 0),
    'GREEN': (0, 220, 40),
    'BLACK': (15, 15, 15),
    'WHITE': '#ffffff',
    'GREY1': '#d1d1d1',
    'GREY2': '#a1a1a1',
    'PINK': '#fc03f8',
    'PURPLE': '#7734eb',
    'ORANGE': '#f5a742',
    'ELEC_BLUE': '#59CBE8'
}
screen_x = 850
screen_y = 765
screen = pg.display.set_mode((screen_x,screen_y))

pg.init()
pg.display.set_caption("Platformer")