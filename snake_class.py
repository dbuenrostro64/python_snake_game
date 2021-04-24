import pygame
from pygame.math import Vector2
import colors

class Snake:

    def __init__(self, win_size, surface):
        self.color = colors.green
        self.pos_x = win_size[0]/2
        self.pos_y = win_size[1]/2
        self.body2 = [Vector2(self.pos_x, self.pos_y), Vector2(self.pos_x-20, self.pos_y), Vector2(self.pos_x-40, self.pos_y)]
        self.block_size = 20
        self.velocity = 20
        self.direction = "none"
        self.direction2 = Vector2(20,0)
        self.surface = surface

    def draw(self):
        for block in self.body2:
            block_rect = pygame.Rect(block.x, block.y, self.block_size, self.block_size)
            pygame.draw.rect(self.surface, self.color, block_rect)

    def move(self):
        body_copy = self.body2[:-1]
        body_copy.insert(0, body_copy[0] + self.direction2)
        self.body2 = body_copy[:]

    def add_block(self):
        pass