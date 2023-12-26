import pygame as pg
from config import *
from logic import *

pg.init()

screen = pg.display.set_mode(DISPLAY)
clock = pg.time.Clock()

snake = Snake([10, 10])
world = World(field)
food = Food([12, 12])

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key in Action.keys:
                action = controller(event.key)
                snake.move(action)

    snake.update()
    world.update(snake, food)
    screen.fill("black")
    world.draw(screen, snake, food)
    pg.display.update()

    clock.tick(FPS)