import pygame
import Varriables
pygame.font.init()

GREEN = (0, 255, 50)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (255, 0, 0)
GREY = (100, 100, 100)
BLACK= (0,0,0)
CYAN= (0, 200, 100)
WIDTH = 600
ROWS = 20
DIS = WIDTH // ROWS
FPS = 10
NUMBER_SIZE = 60
TEXTX = WIDTH/2-75
TEXTH = 50

f1 = pygame.font.Font(None, 24)
text1 = f1.render('В режиме тора змейка может проходить сквозь стены', True,
                  WHITE)
text2= f1.render('В режиме стены змейка не может проходить сквозь стены' , True, WHITE)