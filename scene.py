import pygame
import colors

class Scene:
    def __init__(self, screen):
        self._screen = screen
        self._background = pygame.Surface(self._screen.get_size())
        self._background.fill(colors.purple)
        self._is_valid = True

    def draw(self):
        self._screen.blit(self._background, (0, 0))

    def process_event(self, event):
        print(str(event))
        if event.type == pygame.QUIT:
            print("good bye!")
            self._is_valid = False
        if event.type == pygame.KEYDOWN and event.type == pygame.K_ESCAPE:
            print("bye bye!")
            self._is_valid = False

    def is_valid(self):
        return self._is_valid

    def update(self):
        pass

    class TitleScene(Scene):
        def __init__(self, screen, title, title_color, title_size):
            super().__init__(screen)
            self._background.fill(colors.green)
            title_font = pygame.font.Font(pygame.font.get_default_font(), title_size)
            self._title = title_font.render(title, True, title_color)
            press_any_key_font = pygame.font.Font(pygame.font.get_default_font(), 18)
            self.press_any_key = press_any+key_font.render("press any key.", True, colors.black)
            (w, h) = self._screen.get_size()
            self._title_pos = self._title.get_rect(center=(w/2, h/2))
            self._press_any_key_pos = self. press_any_key.get_rect(center=(w/2, h - 50))

        def draw(self):
            super().draw()
            self._screen.blit(self._title, self._title_pos)
            self._screen.blit(self._press_any_key, self._press_any_key_pos)

        def process_event(self, event):
            super().process_event(event)
            if event.type == pygame.KEYDOWN:
                self._is_valid = False

    class GameLevel(Scene):
        def __init__(self, screen, snake, food, score):
            super().__init__(screen)
            self._background.fill(colors.orange)
            self._screen = screen
            self._snake = snake
            self._food = food
            self._score = score

        def draw(self):
            super().draw()
            self._snake.draw()
            self._food.draw()

        def process_event(self, event):
            super().process_event(event)