import pygame as pg
from config import *

pg.init()

screen = pg.display.set_mode(DISPLAY)
clock = pg.time.Clock()


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    screen.fill("black")
    pg.display.update()

    clock.tick(FPS)