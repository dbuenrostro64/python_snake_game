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
import scenes_class
import leaderboard


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
        font.render_to(surface, (150, 100), "SNAKE GAME!!!", colors.green, None, size=75)
        font.render_to(surface, (125, 400), "Press space to start", colors.green, None, size=50)
        pygame.display.update()

def rules_screen(surface, font):
    """Displays game rules before game """
    pass

def game_over(surface, font, score, high_scores):
    """Draws game over when triggered """
    
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    letter_pos = 0
    name = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    high_scores.append((name, score))
                    leaderboard.save_scores(high_scores)
                    leaderboard_screen(surface, font, score, high_scores)
                elif event.key == pygame.K_RIGHT:
                    letter_pos += 1
                    if letter_pos == 26:
                        letter_pos = 0
                elif event.key == pygame.K_LEFT:
                    letter_pos -= 1
                    if letter_pos == -26:
                        letter_pos = 0
                elif event.key == pygame.K_SPACE:
                    name = name + letters[letter_pos]
        surface.fill(colors.black)
        str_score=str(score)
        font.render_to(surface, (175, 50), "GAME OVER", colors.red, None, size=80)
        font.render_to(surface, (215, 175), "Score: "+str_score, colors.red, None, size=80)
        font.render_to(surface, (100, 280), "Left and right arrow to cycle letters", colors.white, None, size=30)
        font.render_to(surface, (275, 325), "Space to enter", colors.white, None, size=30)
        font.render_to(surface, (275, 375), "Enter Name: " + letters[letter_pos], colors.blue, None, size=30)
        font.render_to(surface, (315, 475), name, colors.blue, None, size=30)
        font.render_to(surface, (250, 525), "enter to confirm", colors.white, None, size=30)

        pygame.display.update()

def leaderboard_screen(surface, font, score, high_scores):
    surface.fill(colors.black)
    str_score=str(score)
    font.render_to(surface, (225, 50), "HIGH SCORES", colors.purple, None, size=50)
    font.render_to(surface, (150, 125), "NAME", colors.purple, None, size=25)
    font.render_to(surface, (550, 125), "SCORE", colors.purple, None, size=25)

    sorted_high_scores = sorted(high_scores, key = lambda x: x[1], reverse=True)
    height = 175
    for scr in sorted_high_scores:
        scr_str=str(scr[1])
        font.render_to(surface, (150, height), scr[0] , colors.blue, None, size=25)
        font.render_to(surface, (550, height), scr_str, colors.blue, None, size=25)
        height += 30
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    sys.exit()

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
    font_obj = font_init()
    play_again = True

    snake_1 = snake_class.Snake(WINDOW_SIZE, background)
    food_1 = food_class.Food(WINDOW_SIZE, background)
    score = 0
    high_scores = leaderboard.load_scores()

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
            play_again = game_over(background, font_obj, score, high_scores)
        if snake_1.body[0].x < 0 or snake_1.body[0].x > WINDOW_WIDTH:
            play_again = game_over(background, font_obj, score, high_scores)
        if snake_1.body[0].y < 0 or snake_1.body[0].y > WINDOW_HEIGHT:
            play_again = game_over(background, font_obj, score, high_scores)       
        if food_collide_check(snake_1, food_1):
            snake_1.grow()
            food_1.randomize()
            score += 1

        seconds = (pygame.time.get_ticks()-start_tick)/1000
        seconds = round(seconds)
        background.fill(colors.blue)
        display_score(background, font_obj, colors.black, score)
        display_time(background, font_obj, colors.white, seconds)
        snake_1.draw()
        food_1.draw()
        pygame.display.update()

if __name__ == '__main__':
    main()
