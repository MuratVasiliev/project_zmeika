import random
import pygame as pg
import classes as cl
import constants as const
import os

import menu

start_length = 1
start_food = 5
BLACK = (0, 0, 0)
GREEN = (0, 255, 50)
RED = (0, 0, 255)
BLUE = (255, 0, 0)
GREY = (100, 100, 100)
dir = [0, 0]
dir1 = [0, 0]
w = 800
# h = 600
rows = 20
dis = w // rows
pg.init()
sn_running = True
screen = pg.display.set_mode((w, w))
all_sprites = pg.sprite.Group()
clock = pg.time.Clock()
fps = 10
foodx = w // 2
foody = w // 2


class Cube:
    def __init__(self, pos):
        self.pos = pos


class Snakes:
    def __init__(self):
        self.list = [Snake([0, 1], [0, 0], BLUE)]

    def add_snake(self, dir, pos, color):
        self.list.append(Snake(dir, pos, color))

    def draw(self):
        for k in self.list:
            for i in k.body:
                if i != k.body[len(k.body) - 1]:  # кроме головы
                    i.surf = pg.Surface((dis, dis))
                    i.surf.fill(k.color)
                    i.rect = i.surf.get_rect(topleft=i.pos)
                    screen.blit(i.surf, i.pos)
                else:  # голова
                    i.surf = pg.Surface((dis, dis))
                    i.surf.fill(pg.Color('#FF0000'))
                    i.rect = i.surf.get_rect(topleft=i.pos)
                    screen.blit(i.surf, i.pos)

    def move(self):
        print('move1')
        for k in self.list:
            k.head = k.body[len(k.body) - 1]
            k.body.append(Cube([k.head.pos[0] + k.dir[0] * dis, k.head.pos[1] + k.dir[1] * dis]))
            k.head = k.body[len(k.body) - 1]
            k.body.pop(0)
            if k.head.pos[0] >= w:
                k.head.pos[0] = 0
            if k.head.pos[0] <= -dis:
                k.head.pos[0] = w - dis
            if k.head.pos[1] >= w:
                k.head.pos[1] = 0
            if k.head.pos[1] <= -dis:
                k.head.pos[1] = w - dis
            print('move2')


class Snake:
    def __init__(self, dir, pos, color):
        self.body = []
        self.body = [Cube(pos)]
        self.dir = dir
        self.running = True
        self.color = color

    def re_dir(self, event):
        if self == snakes.list[0]:
            if event.key == pg.K_UP and self.dir != [0, 1]:
                self.dir = [0, -1]
            if event.key == pg.K_DOWN and self.dir != [0, -1]:
                self.dir = [0, 1]
            if event.key == pg.K_LEFT and self.dir != [1, 0]:
                self.dir = [-1, 0]
            if event.key == pg.K_RIGHT and self.dir != [-1, 0]:
                self.dir = [1, 0]
            print('redir0')
        if self == snakes.list[1]:
            if event.key == pg.K_w and self.dir != [0, 1]:
                self.dir = [0, -1]
            if event.key == pg.K_s and self.dir != [0, -1]:
                self.dir = [0, 1]
            if event.key == pg.K_a and self.dir != [1, 0]:
                self.dir = [-1, 0]
            if event.key == pg.K_d and self.dir != [-1, 0]:
                self.dir = [1, 0]
            print('redir0')

    def add_Cube(self):
        self.body.insert(0, Cube(self.body[0].pos))

    def uyebalsya(self, head_pos):
        for snake in snakes.list:
            for snake_body in snake.body[:-2]:
                if head_pos[0] == snake_body.pos[0] and head_pos[1] == snake_body.pos[1]:
                    # snakes.add_snake([random.randint(0,w),random.randint(0,w)],[0,0],snake.color)
                    self.dir = [0, 0]
                    print('uyebalsya')


class Bigmak:
    def __init__(self):
        self.list = [Food(w)]

    def add_Food(self):
        self.list.append(Food(w))

    def draw(self, screen, dis):
        for food in self.list:
            pg.draw.rect(screen, pg.Color('#3AD044'), [food.x, food.y, dis, dis])


class Food:
    def __init__(self, w):
        self.x = w // 2
        self.y = w // 2
        self.type = 0

    def rand(self):  # рандомайзер еды
        self.x = random.randrange(1, rows) * dis
        self.y = random.randrange(1, rows) * dis

    def eat(self, snake):  # если съел
        for snake in snakes.list:
            if snake.body[len(snake.body) - 1].pos[0] == self.x and snake.body[len(snake.body) - 1].pos[1] == self.y:
                self.rand()
                screen.fill(pg.Color('#A5FFAB'))
                snake.add_Cube()
                print('eated')


def snake_loop1(w, rows, surface):  # сетка
    size_btwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        pg.draw.line(surface, GREY, (x, 0), (x, w))
        pg.draw.line(surface, GREY, (0, y), (w, y))


snakes = Snakes()
snakes.add_snake([0, -1], [0, rows * dis], RED)

bigmak = Bigmak()
for i in range(start_food):
    bigmak.add_Food()

for snake in snakes.list:
    for i in range(start_length):
        snake.add_Cube()

while sn_running:
    pg.display.update()
    clock.tick(fps)
    screen.fill(pg.Color('#EFFFA5'))

    for event in pg.event.get():  # изменение направления и приращение попы на пробел
        if event.type == pg.KEYDOWN:
            for snake in snakes.list:
                snake.re_dir(event)
        if event.type == pg.QUIT:
            exit()
    keys = pg.key.get_pressed()

    if keys[pg.K_SPACE]:
        for snake in snakes.list:
            snake.add_Cube()
    for food in bigmak.list:
        for snake in snakes.list:
            food.eat(snake)
    bigmak.draw(screen, dis)
    # f.draw(screen, dis)  # отрисовка еды
    # f.eat(s.body[len(s.body) - 1].pos[0], s.body[len(s.body) - 1].pos[1])  # проверка на съедение
    # f.eat1(s1.body[len(s1.body) - 1].pos[0], s1.body[len(s1.body) - 1].pos[1])

    for snake in snakes.list:
        snake.uyebalsya(snake.body[len(snake.body) - 1].pos)

    snakes.move()
    snakes.draw()
    draw_grid(w, rows, screen)
