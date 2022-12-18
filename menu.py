import pygame
import Varriabl

class Menu:
    def __init__(self, game):
        """Создаем курсор, который будет двигаться по меню"""
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100
    def draw_cursor(self):
        """Рисуем курсор в форме звезды на экране"""
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)