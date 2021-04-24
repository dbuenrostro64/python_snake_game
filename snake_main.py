import pygame, sys, random, os
import pygame.freetype
from pygame.locals import *
from pygame.math import Vector2
import colors
import snake_class
import food_class


def collision_check(snake, food):
    #if snake.pos_x == food.pos_x and snake.pos_y == food.pos_y: 
    if snake.body2[0] == food.vect_pos:
        return True
    else:
        return False

def font_init():
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"fonts","Boxfont Round.ttf")
    font_size = 64
    pygame.freetype.init()
    myfont = pygame.freetype.Font(font_path, font_size)
    return myfont

def display_score(surface, font, color, score):
    str_score = str(score)
    font.render_to(surface, (600, 25), "Score: " + str_score, color, None, size=32)

def display_game_over(surface, font, color):
    pass

def main():
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
    food_1 = food_class.Food(WINDOW_SIZE)
    score = 0

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    # main game loop
    while True: 
        pygame.time.delay(25)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == SCREEN_UPDATE:
                snake_1.move()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_1.direction = "up"
                elif event.key == pygame.K_DOWN:
                    snake_1.direction = "down"
                elif event.key == pygame.K_LEFT:
                    snake_1.direction = "left"
                elif event.key == pygame.K_RIGHT:
                    snake_1.direction = "right"            

        if snake_1.direction == "up":
            snake_1.direction2 = [0,-20]
        elif snake_1.direction == "down":
            snake_1.direction2 = [0,20]
        elif snake_1.direction == "left":
            snake_1.direction2 = [-20,0]
        elif snake_1.direction == "right":
            snake_1.direction2 = [20,0]  

        #snake_1.move()

        # situation check
        collision = collision_check(snake_1, food_1)
        if collision:
            food_1.randomize()
            score += 1

        background.fill(colors.orange)  
        display_score(background, font_obj, colors.black, score) 
        snake_1.draw()
        #print(snake_1.body2[0])
        #print(food_1.vect_pos)
        #food_1.draw()
        pygame.draw.rect(background, colors.red, pygame.Rect(food_1.pos_x, food_1.pos_y, food_1.size, food_1.size))            
        pygame.display.update()

if __name__ == '__main__':
    main()