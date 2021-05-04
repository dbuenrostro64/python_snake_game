"""File that stores snake class """

import pygame
from pygame.math import Vector2
import colors


class Snake:
    """Creates snake object controlled by the player"""
    def __init__(self, win_size, surface):
        self.color = colors.green
        self.win_size = win_size
        self.pos_x = win_size[0]/2
        self.pos_y = win_size[1]/2
        self.body = [Vector2(self.pos_x, self.pos_y), Vector2(self.pos_x-20, self.pos_y),
                     Vector2(self.pos_x-40, self.pos_y)]
        self.block_size = 20
        self.velocity = 20
        self.key_press = "right"
        self.direction = Vector2(20, 0)
        self.surface = surface
        self.has_eaten = False
        self.growth_num = 3
        self.new_blocks = 0

    def draw(self):
        """Draws snake based on the position of the head and body squares"""
        for block in self.body:
            block_rect = pygame.Rect(block.x, block.y, self.block_size, self.block_size)
            pygame.draw.rect(self.surface, self.color, block_rect)

    def change_direction(self):
        """Changes direction of snake based on 4 directional key presses"""
        if self.key_press == "up":
            self.direction = [0, -20]
        elif self.key_press == "down":
            self.direction = [0, 20]
        elif self.key_press == "left":
            self.direction = [-20, 0]
        elif self.key_press == "right":
            self.direction = [20, 0]

    def move(self):
        """
        Changes position of snake head and all the body squares as snake moves and turns.
        Snake body squares will follow the head like a train by erasing the tail square
        one block movement at a time. If the snake has eaten then the tail square will be
        preserved for growth_num movements
        """
        if self.has_eaten:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            self.new_blocks += 1
            if self.new_blocks == self.growth_num:
                self.new_blocks = 0
                self.has_eaten = False
        elif not self.has_eaten:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def grow(self):
        """Will record if the snake has eaten on a particular movement"""
        self.has_eaten = True

    def tail_collide_check(self):
        """Will check if the head has collided with any of the body squares"""
        for block in self.body[1:]:
            if block == self.body[0]:
                return True
        return False

    def reset(self):
        self.pos_x = self.win_size[0]/2
        self.pos_y = self.win_size[1]/2
        self.body = [Vector2(self.pos_x, self.pos_y), Vector2(self.pos_x-20, self.pos_y),
                     Vector2(self.pos_x-40, self.pos_y)]
        self.key_press = "right"
        self.direction = Vector2(20, 0)