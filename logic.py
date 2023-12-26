from pygame import Vector2

class World:
    def __init__(self):
        pass
    def draw(self, field, snake, food):
        pass

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