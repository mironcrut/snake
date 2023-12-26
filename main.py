import pygame as pg
from config import *
from logic import *

pg.init()

screen = pg.display.set_mode(DISPLAY)
clock = pg.time.Clock()

snake = Snake([10, 10])
world = World()
food = Food([12, 12])

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            action = controller(event.key)
            snake.move(action)

    screen.fill("black")
    world.draw(screen, field, snake, food)
    pg.display.update()

    clock.tick(FPS)