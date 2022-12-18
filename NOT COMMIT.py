import pygame
import Varriables


class Menu:
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.levelx, self.levely = self.mid_w, self.mid_h + 50
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 70
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 90
        self.scorex, self.scorey = self.mid_w, self.mid_h + 110
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
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
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Level 1'
        self.l1x, self.l1y = self.mid_w, self.mid_h + 20
        self.l2x, self.l2y = self.mid_w, self.mid_h + 40
        self.l3x, self.l3y = self.mid_w, self.mid_h + 60
        self.cursor_rect.midtop = (self.l1x + self.offset, self.l1y)
    def display_menu(self):
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



class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Difficulty'
        self.Difx, self.Dify = self.mid_w, self.mid_h + 20
        self.controlsx, self.controlsy = self.mid_w, self.mid_h + 40
        self.cursor_rect.midtop = (self.Difx + self.offset, self.Dify)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Options', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("Difficulty", 15, self.Difx, self.Dify)
            self.game.draw_text("Controls", 15, self.controlsx, self.controlsy)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == 'Difficulty':
                self.state = 'Controls'
                self.cursor_rect.midtop = (
                    self.controlsx + self.offset, self.controlsy)
            elif self.state == 'Controls':
                self.state = 'Difficulty'
                self.cursor_rect.midtop = (self.Difx + self.offset, self.Dify)
        elif self.game.START_KEY:
            if self.state == 'Controls':
                self.game.curr_menu = self.game.controls
            elif self.state == 'Difficulty':
                self.game.curr_menu = self.game.difficulty
            self.run_display = False
            pass


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made in MIPT, Б02-213 Group', 15, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text('Muratov Vasiliy', 15, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 25)
            self.game.draw_text('Pak Boris', 15, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text('Steksov Ivan', 15, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 55)
            self.blit_screen()


class ScoreMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Score:', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('1. ' + str(sorted(Varriables.score)[-1]), 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text('2. ' + str(sorted(Varriables.score)[-2]), 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 30)
            self.game.draw_text('3. ' + str(sorted(Varriables.score)[-3]), 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 50)
            self.blit_screen()


class ControlsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Controls:', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Arrow Keys - change snake direction', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text('BackSpace - return to previous menu', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 30)
            self.game.draw_text('Enter - enter', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 + 50)
            self.blit_screen()


class DifficultyMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = '1'
        self.d1x, self.d1y = self.mid_w, self.mid_h + 20
        self.d2x, self.d2y = self.mid_w, self.mid_h + 40
        self.d3x, self.d3y = self.mid_w, self.mid_h + 60
        self.d4x, self.d4y = self.mid_w, self.mid_h + 80
        self.d5x, self.d5y = self.mid_w, self.mid_h + 100
        self.cursor_rect.midtop = (self.d1x + self.offset, self.d1y)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text('Difficulty', 20, self.game.DISPLAY_W / 2,
                                self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text("1", 15, self.d1x, self.d1y)
            self.game.draw_text("2", 15, self.d2x, self.d2y)
            self.game.draw_text("3", 15, self.d3x, self.d3y)
            self.game.draw_text("4", 15, self.d4x, self.d4y)
            self.game.draw_text("5", 15, self.d5x, self.d5y)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.UP_KEY or self.game.DOWN_KEY:
            if self.state == '1':
                self.state = '2'
                self.cursor_rect.midtop = (self.d2x + self.offset, self.d2y)
            elif self.state == '2':
                self.state = '3'
                self.cursor_rect.midtop = (self.d3x + self.offset, self.d3y)
            elif self.state == '3':
                self.state = '4'
                self.cursor_rect.midtop = (self.d4x + self.offset, self.d4y)
            elif self.state == '4':
                self.state = '5'
                self.cursor_rect.midtop = (self.d5x + self.offset, self.d5y)
            elif self.state == '5':
                self.state = '1'
                self.cursor_rect.midtop = (self.d1x + self.offset, self.d1y)
        elif self.game.START_KEY:
            if self.state == '1':
                self.game.curr_menu = self.game.main_menu
                Varriables.difficulty = 10
            elif self.state == '2':
                self.game.curr_menu = self.game.main_menu
                Varriables.difficulty = 50
            elif self.state == '3':
                self.game.curr_menu = self.game.main_menu
                Varriables.difficulty = 100
            elif self.state == '4':
                self.game.curr_menu = self.game.main_menu
                Varriables.difficulty = 150
            elif self.state == '5':
                self.game.curr_menu = self.game.main_menu
                Varriables.difficulty = 200
            self.run_display = False
            pass
