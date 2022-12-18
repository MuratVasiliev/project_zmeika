import pygame
import Varriables


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

        def display_menu(self):
            """Прописываем пункты меню и заливаем его черным цветом"""
            self.run_display = True
            while self.run_display:
                self.game.check_events()
                self.check_input()
                self.game.display.fill(self.game.BLACK)
                self.game.draw_text('Snake', 20, self.game.DISPLAY_W / 2,
                                    self.game.DISPLAY_H / 2 - 20)
                self.game.draw_text("Start Game", 20, self.startx, self.starty)
                self.game.draw_text("Level", 20, self.levelx, self.levely)
                self.game.draw_text("Options", 20, self.optionsx, self.optionsy)
                self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
                self.game.draw_text("Score", 20, self.scorex, self.scorey)
                self.draw_cursor()
                self.blit_screen()

    def move_cursor(self):
        """Прописываем движение курсора при нажатии клавиш"""
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.levelx + self.offset, self.levely)
                self.state = 'Level'
            elif self.state == 'Level':
                self.cursor_rect.midtop = (
                    self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (
                    self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (
                    self.scorex + self.offset, self.scorey)
                self.state = 'Score'
            elif self.state == 'Score':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.scorex + self.offset, self.scorey)
                self.state = 'Score'
            elif self.state == 'Score':
                self.cursor_rect.midtop = (
                    self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Level':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (
                    self.optionsx + self.offset, self.optionsy)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (
                    self.levelx + self.offset, self.levely)
                self.state = 'Level'

    def check_input(self):
        """Переход при нажатии на пункт меню"""
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Level':
                self.game.curr_menu = self.game.level
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Score':
                self.game.curr_menu = self.game.score
            self.run_display = False


class LevelMenu(Menu):
    """Прописываем положение курсора в Level Menu"""

    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Level 1'
        self.l1x, self.l1y = self.mid_w, self.mid_h + 20
        self.l2x, self.l2y = self.mid_w, self.mid_h + 40
        self.l3x, self.l3y = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.l1x + self.offset, self.l1y)

    def display_menu(self):
        """Прописываем меню при нажатии на Level в главном меню"""
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Level', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Level 1", 15, self.l1x, self.l1y)
            self.game.draw_text("Level 2", 15, self.l2x, self.l2y)
            self.game.draw_text("Level 3", 15, self.l3x, self.l3y)
            self.draw_cursor()
            self.blit_screen()
   def check_input(self):
       """Прописываем движение курсора при нажатии клавиш"""
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY:
            if self.state == 'Level 1':
                self.state = 'Level 3'
                self.cursor_rect.midtop = (
                    self.l3x + self.offset, self.l3y)
            elif self.state == 'Level 3':
                self.state = 'Level 2'
                self.cursor_rect.midtop = (self.l2x + self.offset, self.l2y)
            elif self.state == 'Level 2':
                self.state = 'Level 1'
                self.cursor_rect.midtop = (self.l1x + self.offset, self.l1y)
        elif self.game.DOWN_KEY:
            if self.state == 'Level 1':
                self.state = 'Level 2'
                self.cursor_rect.midtop = (
                    self.l2x + self.offset, self.l2y)
            elif self.state == 'Level 2':
                self.state = 'Level 3'
                self.cursor_rect.midtop = (self.l3x + self.offset, self.l3y)
            elif self.state == 'Level 3':
                self.state = 'Level 1'
                self.cursor_rect.midtop = (self.l1x + self.offset, self.l1y)
        elif self.game.START_KEY:
            if self.state == 'Level 1':
                self.game.curr_menu = self.game.main_menu
                Varriables.lev=1
            elif self.state == 'Level 2':
                self.game.curr_menu = self.game.main_menu
                Varriables.lev=2
            elif self.state == 'Level 3':
                self.game.curr_menu = self.game.main_menu
                Varriables.lev=3
            self.run_display = False
            pass
