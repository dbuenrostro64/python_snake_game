"""File that stores food class """

import random
import pygame
from pygame.math import Vector2
import colors


class Food:
    """Creates food object that can be placed around the game area """
    def __init__(self, win_size, surface):
        self.window_width = win_size[0]
        self.window_height = win_size[1]
        self.pos_x = 100
        self.pos_y = 100
        self.vect_pos = Vector2(self.pos_x, self.pos_y)
        self.size = 20
        self.surface = surface

    def randomize(self):
        """Uses random module to give random position to food object """
        self.pos_x = random.randrange(0, self.window_width, 20)
        self.pos_y = random.randrange(0, self.window_height, 20)
        self.vect_pos = Vector2(self.pos_x, self.pos_y)

    def draw(self):
        """Draws food rectange onto game screen """
        food_rect = pygame.Rect(self.pos_x, self.pos_y, self.size, self.size)
        pygame.draw.rect(self.surface, colors.red, food_rect)
