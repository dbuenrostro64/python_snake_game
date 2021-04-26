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
        self.key_press = "none"
        self.direction = Vector2(20,0)
        self.surface = surface
        self.has_eaten = False
        self.growth_num = 5
        self.new_blocks = 0

    def draw(self):
        for block in self.body2:
            block_rect = pygame.Rect(block.x, block.y, self.block_size, self.block_size)
            pygame.draw.rect(self.surface, self.color, block_rect)

    def move(self):
        if self.has_eaten == True:
            body_copy = self.body2[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body2 = body_copy[:]
            self.new_blocks += 1
            if self.new_blocks == self.growth_num:
                self.new_blocks = 0
                self.has_eaten = False
        elif self.has_eaten == False:
            body_copy = self.body2[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body2 = body_copy[:]

    def grow(self):
        self.has_eaten = True

    def tail_collide_check():
        for block in self.body2[1:]:
            if block == self.body2[0]:
                print("hello")
