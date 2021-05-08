import sys
import pygame
import colors
import leaderboard

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
        font.render_to(surface, (225, 450), "Press space", colors.green, None, size=50)
        pygame.display.update()

def rules_screen(surface, font):
    """Displays game rules before game """
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
        font.render_to(surface, (200, 100), "Use arrow keys to move", colors.green, None, size=30)
        font.render_to(surface, (100, 150), "Eat food to grow and increase score", colors.green, None, size=30)
        font.render_to(surface, (200, 200), "Dont touch your own tail", colors.green, None, size=30)
        font.render_to(surface, (125, 250), "Don't touch the edge of the screen", colors.green, None, size=30)
        font.render_to(surface, (225, 500), "Press space to start", colors.green, None, size=30)
        pygame.display.update()

def run_intro(surface, font):
    start_screen(surface, font)
    rules_screen(surface, font)

def game_over(surface, font, score, high_scores):
    """Draws game over when triggered """
    play_again = False
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
                'O','P','Q','R','S','T','U','V','W','X','Y','Z']
    letter_pos = 0
    name = ""
    while True:
        if play_again == True:
            return play_again
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    high_scores.append((name, score))
                    leaderboard.save_scores(high_scores)
                    play_again = leaderboard_screen(surface, font, score, high_scores)
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
    font.render_to(surface, (100, 500), "(y) to play again", colors.purple, None, size=25)
    font.render_to(surface, (550, 500), "(n) to exit", colors.purple, None, size=25)


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
                if event.key == pygame.K_n:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_y:
                    play_again = True
                    return play_again