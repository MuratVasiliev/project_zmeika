import pygame
import Varriables
pygame.font.init()

GREEN = (0, 255, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (100, 100, 100)
BLACK = (0, 0, 0)
CYAN = (0, 200, 100)
WIDTH = 600
ROWS = 15
DIS = WIDTH // ROWS
FPS = 6
NUMBER_SIZE = 60
TEXTX = WIDTH/2-75
TEXTH = 50

f1 = pygame.font.Font(None, 24)
f2 = pygame.font.Font(None, 36)
text1 = f1.render('В режиме тора змейка может проходить сквозь стены', True,
                  WHITE)
text2 = f1.render('В режиме стены змейка не может проходить сквозь стены' , True, WHITE)
text3 = f1.render('В режиме PVP два игрока сражаются на двух змейках', True, WHITE)

text4 = f2.render('Стексов Иван', True, RED)
text5 = f2.render('Муратов Василий', True, BLUE)
text6 = f2.render('Пак Борис', True, WHITE)