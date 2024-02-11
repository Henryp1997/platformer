import pygame as pg
import os

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
screen_x = 970
screen_y = 730
screen = pg.display.set_mode((screen_x,screen_y))

assets_path = f'{os.path.dirname(os.path.abspath(__file__))}/assets'

pg.init()
pg.display.set_caption("Platformer")