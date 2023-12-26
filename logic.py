import random

import pygame as pg
from pygame import Vector2
from config import *

pg.init()

class World:

    def __init__(self, field):
        self.field = field

    def draw(self, screen, snake, food):
        for y in range(FIELD_HEIGHT):
            for x in range(FIELD_WIDTH):
                color = COLOR_GROUND
                if Vector2(y, x) == snake.pos:
                    color = COLOR_SNAKE_HEAD
                elif Vector2(y, x) == food.pos:
                    color = COLOR_FOOD
                elif self.field[y][x] > 0:
                    color = COLOR_SNAKE_BODY
                pos = x * SIZE + SIZE // 2, y * SIZE + SIZE // 2
                pg.draw.circle(screen, color, pos, SIZE // 2, 5)

    def update(self, snake, food):
        x, y = snake.pos
        self.field[int(x)][int(y)] = snake.length
        if snake.pos == food.pos:
            snake.level_up()
            food.respawn()
            return
        for y in range(FIELD_HEIGHT):
            for x in range(FIELD_WIDTH):
                self.field[y][x] = max(0, self.field[y][x] - 1)

class Food:
    def __init__(self, pos=None):
        if pos is None:
            self.respawn()
        else:
            self.pos = Vector2(pos)

    def respawn(self):
        x = random.randint(0, FIELD_WIDTH - 1)
        y = random.randint(0, FIELD_HEIGHT - 1)
        self.pos = Vector2(x, y)
class Action:
    keys = [pg.K_w, pg.K_s, pg.K_a, pg.K_d]
    up = Vector2(-1, 0)
    down = Vector2(1, 0)
    right = Vector2(0, 1)
    left = Vector2(0, -1)
def controller(key):
    if key == pg.K_w:
        return Action.up
    if key == pg.K_s:
        return Action.down
    if key == pg.K_a:
        return Action.left
    if key == pg.K_d:
        return Action.right

class Snake:
    def __init__(self, pos):
        self.pos = Vector2(pos)
        self.dir = Action.up
        self.length = START_LENGTH

    def update(self):
        print(self.pos, self.dir)
        x = (self.pos.x + self.dir.x) % FIELD_WIDTH
        y = (self.pos.y + self.dir.y) % FIELD_HEIGHT
        self.pos = Vector2(x, y)

    def level_up(self):
        self.length += 1
    def move(self, dir: Vector2):
        self.dir = dir

