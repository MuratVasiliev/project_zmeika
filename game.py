import pygame
import menu
import snake


class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 480, 270
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.BLACK, self.WHITE, self.BLUE = (0, 0, 0), (255, 255, 255), (0, 253, 255) # цвета
        self.main_menu = menu.MainMenu(self)
        self.level = menu.LevelMenu(self)
        self.options = menu.OptionsMenu(self)
        self.difficulty = menu.DifficultyMenu(self)
        self.credits = menu.CreditsMenu(self)
        self.controls = menu.ControlsMenu(self)
        self.score = menu.ScoreMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            snake.snake_loop()
            self.playing = False

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
