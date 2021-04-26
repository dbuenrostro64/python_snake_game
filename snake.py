import pygame, sys, os
import pygame.freetype
from pygame.locals import *
import colors
import snake_class
import food_class


def food_collide_check(snake, food):
    if snake.body[0] == food.vect_pos:
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

def display_time(surface, font, color, time):
    str_time = str(time)
    font.render_to(surface, (50,25), "Time: " + str_time, color, None, size=32)

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
    food_1 = food_class.Food(WINDOW_SIZE, background)
    score = 0

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)
    seconds = 0
    start_tick = pygame.time.get_ticks()

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
                if event.key == pygame.K_UP and snake_1.key_press != "down":
                    snake_1.key_press = "up"
                elif event.key == pygame.K_DOWN and snake_1.key_press != "up":
                    snake_1.key_press = "down"
                elif event.key == pygame.K_LEFT and snake_1.key_press != "right":
                    snake_1.key_press = "left"
                elif event.key == pygame.K_RIGHT and snake_1.key_press != "left":
                    snake_1.key_press = "right"            

        if snake_1.key_press == "up": 
            snake_1.direction = [0,-20]
        elif snake_1.key_press == "down": 
            snake_1.direction = [0,20]
        elif snake_1.key_press == "left":
            snake_1.direction = [-20,0]
        elif snake_1.key_press == "right":
            snake_1.direction = [20,0]  

        # situation check
        snake_1.tail_collide_check()
        if food_collide_check(snake_1, food_1):
            snake_1.grow()
            food_1.randomize()
            score += 1

        if score >= 5:
            display_game_over(background, font_obj, colors.red)

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
