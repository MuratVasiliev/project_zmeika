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

    def blit_screen(self):
        """Отрисовываем постоянную картинку"""
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        """Пишем положение курсора на разных позициях"""
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.levelx, self.levely = self.mid_w, self.mid_h + 50
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 70
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.scorex, self.scorey = self.mid_w, self.mid_h + 110
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)