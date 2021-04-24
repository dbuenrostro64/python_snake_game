import pygame, random
from pygame.math import Vector2

class Food:

    def __init__(self, win_size):
        self.window_width = win_size[0]
        self.window_height = win_size[1]
        self.pos_x = 100
        self.pos_y = 100
        self.vect_pos = Vector2(self.pos_x, self.pos_y)
        self.size = 20

    def randomize(self):
        self.pos_x = random.randrange(0, self.window_width, 20) 
        self.pos_y = random.randrange(0, self.window_height, 20)
        self.vect_pos = Vector2(self.pos_x, self.pos_y)

    def spawn_food(self):
        pass