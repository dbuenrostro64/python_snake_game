import pygame, sys, random, os
import pygame.freetype
from pygame.locals import *
from pygame.math import Vector2


class Snake:

    def __init__(self, win_size, surface):

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
            pygame.draw.rect(self.surface, (183,191,122), block_rect)

    def move(self):
        body_copy = self.body2[:-1]
        body_copy.insert(0, body_copy[0] + self.direction2)
        self.body2 = body_copy[:]

    def add_block(self):
        pass


class Food:

    def __init__(self, win_size):
        self.window_width = win_size[0]
        self.window_height = win_size[1]
        self.pos_x = 100
        self.pos_y = 100
        self.size = 20

    def randomize(self):
        self.pos_x = random.randrange(0, self.window_width, 20) 
        self.pos_y = random.randrange(0, self.window_height, 20)

    def spawn_food(self):
        pass


def collision_check(snake, food):
    if snake.pos_x == food.pos_x and snake.pos_y == food.pos_y: 
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

    # colors
    black = pygame.Color(0, 0, 0)
    white = pygame.Color(255, 255, 255)
    orange = pygame.Color(227, 185, 30)
    green = pygame.Color(40, 162, 21)
    red = pygame.Color(199, 0, 57)

    # game init
    pygame.init()
    pygame.display.set_caption('Snake Game')
    background = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    background.fill(orange)
    font_obj = font_init()

    snake_1 = Snake(WINDOW_SIZE, background)
    food_1 = Food(WINDOW_SIZE)
    score = 0

    SCREEN_UPDATE = pygame.USEREVENT
    pygame.time.set_timer(SCREEN_UPDATE, 150)

    # main game loop
    while True: 
        pygame.time.delay(100)

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
            pass
            #snake_1.pos_y -= snake_1.velocity
            snake_1.direction2 = [0,-20]
        elif snake_1.direction == "down":
            pass
            #snake_1.pos_y += snake_1.velocity
            snake_1.direction2 = [0,20]
        elif snake_1.direction == "left":
            pass
            #snake_1.pos_x -= snake_1.velocity
            snake_1.direction2 = [-20,0]
        elif snake_1.direction == "right":
            pass
            #snake_1.pos_x += snake_1.velocity 
            snake_1.direction2 = [20,0]  

        #snake_1.move()

        # situation check
        collision = collision_check(snake_1, food_1)
        if collision:
            food_1.randomize()
            score += 1

        background.fill(orange)  
        display_score(background, font_obj, black, score) 
        snake_1.draw()
        #pygame.draw.rect(background, green, pygame.Rect(snake_1.pos_x, snake_1.pos_y, snake_1.block_size, snake_1.block_size)) 
        pygame.draw.rect(background, red, pygame.Rect(food_1.pos_x, food_1.pos_y, food_1.size, food_1.size))            
        pygame.display.update()

if __name__ == '__main__':
    main()
