"""This code will run the main game using the snake and food classes imported """

# Diego Buenrostro
# CPSC 386-01
# 04-27-2021
# dbuenrostro64@csu.fullerton.edu
# @dbuenrostro64
#
# Snake Game
#
# Implementation of classic game of Snake
#

import os
import sys
import pygame
import pygame.freetype
from pygame.locals import *
import colors
import snake_class
import food_class


def food_collide_check(snake, food):
    """Return True if snake head and food collide """
    return snake.body[0] == food.vect_pos

def font_init():
    """Initialize font file for use later """
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             "fonts", "Boxfont Round.ttf")
    font_size = 64
    pygame.freetype.init()
    myfont = pygame.freetype.Font(font_path, font_size)
    return myfont

def display_score(surface, font, color, score):
    """Draws updated score onto the screen """
    str_score = str(score)
    font.render_to(surface, (600, 25), "Score: " + str_score, color, None, size=32)

def display_time(surface, font, color, time):
    """Draws time in seconds onto the screen"""
    str_time = str(time)
    font.render_to(surface, (50, 25), "Time: " + str_time, color, None, size=32)

def start_screen(surface, font):
    """Draws start menu before the game """
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = False
        surface.fill(colors.purple)
        font.render_to(surface, (150, 100), "SNAKE GAME!!!", colors.black, None, size=75)
        font.render_to(surface, (125, 400), "Press space to start", colors.black, None, size=50)
        pygame.display.update()

def game_over(surface, font):
    """Draws game over when triggered """
    end = True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()
        surface.fill(colors.orange)
        font.render_to(surface, (150, 100), "GAME OVER", colors.red, None, size=100)
        pygame.display.update()

def main():
    """Main game function """
    # window size
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

    # game init
    pygame.init()
    pygame.display.set_caption('Snake Game')
    background = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    background.fill(colors.orange)
    font_obj = font_init()

    snake_1 = snake_class.Snake(WINDOW_SIZE, background)
    food_1 = food_class.Food(WINDOW_SIZE, background)
    score = 0

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)
    seconds = 0
    start_tick = pygame.time.get_ticks()

    start_screen(background, font_obj)

    # main game loop
    while True:
        pygame.time.delay(25)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == SCREEN_UPDATE:
                snake_1.move()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_1.key_press != "down":
                    snake_1.key_press = "up"
                elif event.key == pygame.K_DOWN and snake_1.key_press != "up":
                    snake_1.key_press = "down"
                elif event.key == pygame.K_LEFT and snake_1.key_press != "right":
                    snake_1.key_press = "left"
                elif event.key == pygame.K_RIGHT and snake_1.key_press != "left":
                    snake_1.key_press = "right"

        snake_1.change_direction()

        # situation check
        if snake_1.tail_collide_check():
            game_over(background, font_obj)
        if food_collide_check(snake_1, food_1):
            snake_1.grow()
            food_1.randomize()
            score += 1

        if score >= 5:
            game_over(background, font_obj)

        seconds = (pygame.time.get_ticks()-start_tick)/1000
        seconds = round(seconds)
        background.fill(colors.orange)
        display_score(background, font_obj, colors.black, score)
        display_time(background, font_obj, colors.white, seconds)
        snake_1.draw()
        food_1.draw()
        pygame.display.update()

if __name__ == '__main__':
    main()
