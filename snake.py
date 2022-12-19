import pygame
import random
import pygame

BLACK = (0, 0, 0)
GREEN = (0, 255, 50)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
GREY = (100, 100, 100)
dir = [1, 0]
w = 600
# h = 600
rows = 10
dis = w // rows
pygame.init()
sn_running = True
screen = pygame.display.set_mode((w, w))
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
fps = 15
foodx = w // 2
foody = w // 2


class Cube:
    def __init__(self, pos):
        self.pos = pos


class Snake:
    def __init__(self):
        self.body = []
        self.body = [Cube([0, 0])]

    def add_Cube(self):
        self.body.insert(0, Cube(self.body[0].pos))

    def move(self):
        self.head = self.body[len(self.body) - 1]
        self.body.append(Cube([self.head.pos[0] + dir[0] * dis, self.head.pos[1] + dir[1] * dis]))
        self.head = self.body[len(self.body) - 1]
        self.body.pop(0)
        if self.head.pos[0] >= w:
            self.head.pos[0] = 0
        if self.head.pos[0] <= -dis:
            self.head.pos[0] = w - dis
        if self.head.pos[1] >= w:
            self.head.pos[1] = 0
        if self.head.pos[1] <= -dis:
            self.head.pos[1] = w - dis

    def draw(self):
        for i in self.body:
            if i != self.body[len(self.body) - 1]:  # кроме головы
                i.surf = pygame.Surface((dis, dis))
                i.surf.fill(pygame.Color('#D03E3A'))
                i.rect = i.surf.get_rect(topleft=i.pos)
                screen.blit(i.surf, i.pos)
            else:  # голова
                i.surf = pygame.Surface((dis, dis))
                i.surf.fill(pygame.Color('#FF0000'))
                i.rect = i.surf.get_rect(topleft=i.pos)
                screen.blit(i.surf, i.pos)


class Food:
    def __init__(self, w):
        self.x = w // 2
        self.y = w // 2

    def rand(self):  # рандомайзер еды
        self.x = random.randrange(1, rows) * dis
        self.y = random.randrange(1, rows) * dis

    def draw(self, screen, dis):  # отрисовка еды
        pygame.draw.rect(screen, pygame.Color('#3AD044'), [self.x, self.y, dis, dis])

    def eat(self, snakex, snakey):  # если съел
        if snakex == self.x and snakey == self.y:
            while self.check():
                self.rand()
            screen.fill(pygame.Color('#A5FFAB'))
            s.add_Cube()
            print('eated')

    def check(self):
        for cube_number in range(len(s.body)):
            if self.x == s.body[cube_number].pos[0] and self.y == s.body[cube_number].pos[1]:
                return True
            else:
                self.rand


def draw_grid(w, rows, surface):  # сетка
    size_btwn = w // rows

    x = 0
    y = 0
    for line_number in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(surface, GREY, (x, 0), (x, w))
        pygame.draw.line(surface, GREY, (0, y), (w, y))


s = Snake()  # инициализация анаконды
f = Food(w)  # яблОчко
while sn_running:
    pygame.display.update()
    clock.tick(fps)
    screen.fill(pygame.Color('#EFFFA5'))

    for event in pygame.event.get():  # изменение направления и приращение попы на пробел
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dir != [0, 1]:
                dir = [0, -1]
            if event.key == pygame.K_DOWN and dir != [0, -1]:
                dir = [0, 1]
            if event.key == pygame.K_LEFT and dir != [1, 0]:
                dir = [-1, 0]
            if event.key == pygame.K_RIGHT and dir != [-1, 0]:
                dir = [1, 0]
            if event.key == pygame.K_SPACE:
                s.add_Cube()
        if event.type == pygame.QUIT:
            exit()

    f.check()
    f.draw(screen, dis)  # отрисовка еды
    f.eat(s.body[len(s.body) - 1].pos[0], s.body[len(s.body) - 1].pos[1])  # проверка на съедение
    s.move()  # хуюв
    for event in s.body[:-1]:  # проверка на самопересечение
        if s.head.pos == event.pos:

            # screen.blit(game_over_screen, (0,0))
            print('fuck')

    s.draw()  # хуёу
    draw_grid(w, rows, screen)
