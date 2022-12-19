import pygame as pg
class NumVariables:
    """Class of numeric variables"""

    def __init__(self, num=0):
        self._num = num

    def adder(self, arg):
        self._num += arg

    def setter(self, arg):
        self._num = arg

    def getter(self):
        return self._num

class BullVariables:
    """Class of Bullian variables"""

    def __init__(self, init_bul=True):
        self._bul = init_bul

    def setter(self, arg):
        self._bul = arg

    def changer(self):
        if self._bul:
            self._bul = False
        else:
            self._bul = True

    def getter(self):
        return self._bul

class Button:

    def init(self, x, y, xsize, ysize, text):
        """ constructor of class "Button" """
        self.x = x
        self.y = y
        self.text = text
        self.xsize = xsize
        self.ysize = ysize

    def is_click(self, event):
        """ return True if you click on the Button """
        if self.x < event.pos[0] < self.x + self.xsize and self.y < event.pos[1] < self.y + self.ysize:
            return True

    def write_text_on_button(self, screen):
        """ writing text on the element of class "Button" """
        my_font = pg.font.SysFont("monospace", 30)
        text = my_font.render(str(self.text), 1, (255, 255, 255))
        screen.blit(text, (self.x, self.y))