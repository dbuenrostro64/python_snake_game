import pygame, sys
from pygame.locals import *


def main():
    # window size
    window_width = 800
    window_height = 600

    # colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    orange = pygame.Color(227, 185, 30)
    green = pygame.Color(40, 162, 21)

    pygame.init()
    pygame.display.set_caption('Snake Game')
    background = pygame.display.set_mode((window_width, window_height))
    background.fill(orange)

    square_pos_x = window_width/2
    square_pos_y = window_height/2
    square_side = 30
    square_velocity = 5
    snake_direction = "none"

    while True: # main game loop
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake_direction = "up"
                elif event.key == pygame.K_DOWN:
                    snake_direction = "down"
                elif event.key == pygame.K_LEFT:
                    snake_direction = "left"
                elif event.key == pygame.K_RIGHT:
                    snake_direction = "right"            

        if snake_direction == "up":
            square_pos_y -= square_velocity
        elif snake_direction == "down":
            square_pos_y += square_velocity
        elif snake_direction == "left":
            square_pos_x -= square_velocity
        elif snake_direction == "right":
            square_pos_x += square_velocity    

        background.fill(orange)   
        pygame.draw.rect(background, green, (square_pos_x, square_pos_y, square_side, square_side))             
        pygame.display.update()

if __name__ == '__main__':
    main()
