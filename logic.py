import pygame as pg
from pygame import Vector2
from config import *

pg.init()

class World:
    @staticmethod
    def draw(screen, field, snake, food):
        for y in range(FIELD_HEIGHT):
            for x in range(FIELD_WIDTH):
                color = COLOR_GROUND
                if Vector2(y, x) == snake.pos:
                    color = COLOR_SNAKE_HEAD
                elif Vector2(y, x) == food.pos:
                    color = COLOR_FOOD
                elif field[y][x] > 0:
                    color = COLOR_SNAKE_BODY
                pos = x * SIZE + SIZE // 2, y * SIZE + SIZE // 2
                pg.draw.circle(screen, color, pos, SIZE // 2, 5)

class Food:
    def __init__(self, pos):
        self.pos = Vector2(pos)
class Action:
    up = Vector2(-1, 0)
    down = Vector2(1, 0)
    right = Vector2(0, 1)
    left = Vector2(0, -1)
def controller(key):
    return Action.up

class Snake:
    def __init__(self, pos):
        self.pos = Vector2(pos)
        self.dir = Action.up

    def move(self, action: Action):
        pass