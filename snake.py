
import random
import pygame as pg
import classes as cl
import constants as const


direction_x = cl.NumVariables(1)
direction_y = cl.NumVariables(0)

pg.init()
sn_running = cl.BullVariables(False)
screen = pg.display.set_mode((const.width, const.width))
all_sprites = pg.sprite.Group()
clock = pg.time.Clock()

font_style = pg.font.SysFont("bahnschrift", 25)
score_font = pg.font.SysFont("Elektra", 35)

score = cl.NumVariables()

class Snake:
    def __init__(self):
        self.body = []
        self.body = [cl.Cube([0, 0])]

    def add_Cube(self):
        self.body.insert(0, cl.Cube(self.body[0].pos))

    def move(self):
        self.head = self.body[len(self.body) - 1]
        self.body.append(
            cl.Cube([self.head.pos[0] + direction_x.getter() * const.dis, self.head.pos[1] + direction_y.getter() * const.dis]))
        self.head = self.body[len(self.body) - 1]
        self.body.pop(0)
        if self.head.pos[0] >= const.width:
            self.head.pos[0] = 0
        if self.head.pos[0] <= -const.dis:
            self.head.pos[0] = const.width - const.dis
        if self.head.pos[1] >= const.width:
            self.head.pos[1] = 0
        if self.head.pos[1] <= -const.dis:
            self.head.pos[1] = const.width - const.dis

    def draw(self):
        for i in self.body:
            if i != self.body[len(self.body) - 1]:  # кроме головы
                i.surf = pg.Surface((const.dis, const.dis))
                i.surf.fill(pg.Color('#D03E3A'))
                i.rect = i.surf.get_rect(topleft=i.pos)
                screen.blit(i.surf, i.pos)
            else:  # голова
                i.surf = pg.Surface((const.dis, const.dis))
                i.surf.fill(pg.Color('#FF0000'))
                i.rect = i.surf.get_rect(topleft=i.pos)
                screen.blit(i.surf, i.pos)


class Food:
    def __init__(self):
        self.x = random.randrange(1, const.rows) * const.dis
        self.y = random.randrange(1, const.rows) * const.dis

    def rand(self):  # рандомайзер еды
        self.x = random.randrange(1, const.rows) * const.dis
        self.y = random.randrange(1, const.rows) * const.dis

    def draw(self, screen, dis):  # отрисовка еды
        pg.draw.rect(screen, pg.Color('#3AD044'), [self.x, self.y, dis, dis])

    def eat(self, snakex, snakey):  # если съел
        if snakex == self.x and snakey == self.y:
            while self.check():
                self.rand()
            screen.fill(pg.Color('#A5FFAB'))
            snake.add_Cube()
            print('eated')
            score.adder(1)

    def check(self):
        for cube_number in range(len(snake.body)):
            if self.x == snake.body[cube_number].pos[0] and self.y == snake.body[cube_number].pos[1]:
                return True
            else:
                self.rand

def your_score(score):
    value = score_font.render(f'Your Score: {score.getter()}', True, (0, 0, 0))
    screen.blit(value, [30, 30])







def draw_grid(width, rows, surface):  # сетка
    size_between = width // rows

    x = 0
    y = 0
    for line_number in range(rows):
        x = x + size_between
        y = y + size_between

        pg.draw.line(surface, const.GREY, (x, 0), (x, width))
        pg.draw.line(surface, const.GREY, (0, y), (width, y))


snake = Snake()  # инициализация анаконды
food = Food()  # яблОчко


def snake_loop():
    pg.display.update()
    clock.tick(const.fps)
    screen.fill(pg.Color('#EFFFA5'))
    your_score(score)
    for event in pg.event.get():  # изменение направления и приращение попы на пробел
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and direction_y.getter() != 1:
                direction_x.setter(0)
                direction_y.setter(-1)
            if event.key == pg.K_DOWN and direction_y.getter() != -1:
                direction_x.setter(0)
                direction_y.setter(1)
            if event.key == pg.K_LEFT and direction_x.getter() != 1:
                direction_x.setter(-1)
                direction_y.setter(0)
            if event.key == pg.K_RIGHT and direction_x.getter() != -1:
                direction_x.setter(1)
                direction_y.setter(0)
            if event.key == pg.K_SPACE:
                snake.add_Cube()
        if event.type == pg.QUIT:
            exit()

    food.check()
    food.draw(screen, const.dis)  # отрисовка еды
    food.eat(snake.body[len(snake.body) - 1].pos[0], snake.body[len(snake.body) - 1].pos[1])  # проверка на съедение
    snake.move()  # хуюв
    for event in snake.body[:-1]:  # проверка на самопересечение
        if snake.head.pos == event.pos:
            pass
            # screen.blit(game_over_screen, (0,0))
            #print('fuck')

    snake.draw()  # хуёу
    draw_grid(const.width, const.rows, screen)
