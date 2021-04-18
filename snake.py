import pygame, sys, random
from pygame.locals import *

class Snake:

    def __init__(self, win_size):

        self.snake_pos_x = win_size[0]/2
        self.snake_pos_y = win_size[1]/2
        self.snake_block_size = 30
        self.snake_velocity = 10
        self.snake_direction = "none"

    def add_block(self):
        pass

class Food:

    def __init__(self, win_size):
        self.window_width = win_size[0]
        self.window_height = win_size[1]
        self.food_pos_x = 100
        self.food_pos_y = 100
        self.food_size = 15

    def randomize_food(self):
        self.food_pos_x = random.randrange(1, (window_width//10)) * 10
        self.food_pos_y = random.randrange(1, (window_height//10)) * 10

    def spawn_food(self):
        pass

def main():
    # window size
    window_width = 800
    window_height = 600
    window_size = (window_width, window_height)

    # colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    orange = pygame.Color(227, 185, 30)
    green = pygame.Color(40, 162, 21)
    red = pygame.Color(199, 0, 57)

    # game init
    pygame.init()
    pygame.display.set_caption('Snake Game')
    background = pygame.display.set_mode((window_width, window_height))
    background.fill(orange)

    square_pos_x = window_width/2
    square_pos_y = window_height/2
    square_side = 30
    square_velocity = 10
    snake_direction = "none"

    food_1 = Food(window_size)

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
        pygame.draw.rect(background, red, pygame.Rect(food_1.food_pos_x, food_1.food_pos_y, food_1.food_size, food_1.food_size))            
        pygame.display.update()

if __name__ == '__main__':
    main()
