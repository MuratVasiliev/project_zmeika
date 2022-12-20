import random
import pygame as pg
import pygame
import classes as cl
import constants as const
import menu

counter_food = 0
d = 0
damage = 5
counter_food_max = 15
counter_gnil_max = 30
counter_gnil = 0
counter_delete = 0
counter_delete_max = 50
start_length = 1
start_food = 5
BLACK = (0, 0, 0)
GREEN = (72, 224, 56)
RED = (246, 71, 61)
BLUE = (246, 214, 61)
GREY = (100, 100, 100)
dir = [0, 0]
dir1 = [0, 0]
w = 600
# h = 600
rows = 40
dis = w // rows
pygame.init()
sn1_running = cl.BullVariables(False)
screen = pygame.display.set_mode((w, w))
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
fps = 25
foodx = w // 2
foody = w // 2


class Cube:
    def __init__(self, pos):
        self.pos = pos


class Snakes:
    def __init__(self):
        self.list = [Snake([0, 1], [0, 0], BLUE, 0)]

    def add_snake(self, dir, pos, color, num):
        self.list.append(Snake(dir, pos, color, num))

    def draw(self):
        for k in self.list:
            for i in k.body:
                if i != k.body[len(k.body) - 1]:  # кроме головы
                    i.surf = pygame.Surface((dis, dis))
                    i.surf.fill(k.color)
                    i.rect = i.surf.get_rect(topleft=i.pos)
                    screen.blit(i.surf, i.pos)
                else:  # голова
                    i.surf = pygame.Surface((dis, dis))
                    i.surf.fill(pygame.Color('#FF0000'))
                    i.rect = i.surf.get_rect(topleft=i.pos)
                    screen.blit(i.surf, i.pos)

    def move(self):
        print('move1')
        for k in self.list:
            k.head = k.body[len(k.body) - 1]
            k.body.append(Cube([k.head.pos[0] + k.dir[0] * dis, k.head.pos[1] + k.dir[1] * dis]))
            k.head = k.body[len(k.body) - 1]
            k.body.pop(0)
            # if k.head.pos[0] >= w:
            #     k.head.pos[0] = 0
            # if k.head.pos[0] <= -dis:
            #     k.head.pos[0] = w - dis
            # if k.head.pos[1] >= w:
            #     k.head.pos[1] = 0
            # if k.head.pos[1] <= -dis:
            #     k.head.pos[1] = w - dis
            print('move2')



class Snake:
    def __init__(self, dir, pos, color, num):
        self.body = []
        self.body = [Cube(pos)]
        self.dir = dir
        self.running = True
        self.color = color
        self.num = num
        self.poison = False

    def re_dir(self, event):
        if self.num == 0:
            if event.key == pygame.K_UP and self.dir != [0, 1]:
                self.dir = [0, -1]
            if event.key == pygame.K_DOWN and self.dir != [0, -1]:
                self.dir = [0, 1]
            if event.key == pygame.K_LEFT and self.dir != [1, 0]:
                self.dir = [-1, 0]
            if event.key == pygame.K_RIGHT and self.dir != [-1, 0]:
                self.dir = [1, 0]
            print('redir0')
        if self.num == 1:
            if event.key == pygame.K_w and self.dir != [0, 1]:
                self.dir = [0, -1]
            if event.key == pygame.K_s and self.dir != [0, -1]:
                self.dir = [0, 1]
            if event.key == pygame.K_a and self.dir != [1, 0]:
                self.dir = [-1, 0]
            if event.key == pygame.K_d and self.dir != [-1, 0]:
                self.dir = [1, 0]
            print('redir0')
    def add_Cube(self):
        self.body.insert(0, Cube(self.body[0].pos))

    def delete_Cube(self):
        self.body.pop(0)

    def uyebalsya(self, head_pos):
        temp = 0
        for snake in snakes.list:
            if head_pos[0] >= w or head_pos[0] <= -dis or head_pos[1] >= w or head_pos[1] <= -dis:
                snakes.list[self.num] = Snake([0, 0],
                                                  [(rows - 1) * dis * self.num, (rows - 1) * dis * self.num],
                                                  self.color, self.num)
                snakes.list[snake.num] = snake
                self.dir = [0, 0]
                for cube in self.body:
                    bigmak.add_Food(cube.pos[0], cube.pos[1], 0, (255,255,255))

            if snake != self:
                for snake_body in snake.body:
                    if head_pos[0] == snake_body.pos[0] and head_pos[1] == snake_body.pos[1] and len(snakes.list) <= 2:
                        for cube in self.body:
                            bigmak.add_Food(cube.pos[0], cube.pos[1], 0, (255,255,255))
                        snakes.list[self.num] = Snake([0, 0],
                                                      [(rows - 1) * dis * self.num, (rows - 1) * dis * self.num],
                                                      self.color, self.num)
                        snakes.list[snake.num] = snake
                        self.dir = [0, 0]
                        print('uyebalsya')
            else:
                for snake_body in snake.body[:-2]:
                    if head_pos[0] == snake_body.pos[0] and head_pos[1] == snake_body.pos[1] and len(snakes.list) <= 2:
                        # for cube in self.body:
                        #     bigmak.add_Food(cube.pos[0], cube.pos[1], 0, (255,255,255))
                        snakes.list[self.num] = Snake([0, 0],
                                                      [(rows - 1) * dis * self.num, (rows - 1) * dis * self.num],
                                                      self.color, self.num)
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


class Bigmak:
    def __init__(self):
        self.list = [Food(w // 2, w // 2, 0, (255,255,255))]

    def add_Food(self, x, y, typ, color):
        self.list.append(Food(x, y, typ, color))

    def draw(self, screen, dis):
        for food in self.list:
            pygame.draw.rect(screen, food.color, [food.x, food.y, dis, dis])


class Food:
    def __init__(self, x, y, typ, color):
        self.x = x
        self.y = y
        self.typ = typ
        self.color = color

    def gniloy(self):
        if self.typ == 1:
            self.color = (100, 255, 83)

    def rand(self):  # рандомайзер еды
        self.x = random.randrange(1, rows) * dis
        self.y = random.randrange(1, rows) * dis

    def eat(self, snake):  # если съел
        for snake in snakes.list:
            if snake.body[len(snake.body) - 1].pos[0] == self.x and snake.body[len(snake.body) - 1].pos[1] == self.y:
                self.rand()
                # screen.fill(pygame.Color('#A5FFAB'))
                if self.typ == 0:
                    snake.add_Cube()
                elif self.typ == 1 and len(snake.body) > 1:
                        global d
                        d = damage
                        snake.poison = True

                print('eated')


def draw_grid(w, rows, surface):  # сетка
    size_btwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(surface, GREY, (x, 0), (x, w))
        pygame.draw.line(surface, GREY, (0, y), (w, y))




snakes = Snakes()
snakes.add_snake([0, -1], [0, rows * dis], RED, 1)

bigmak = Bigmak()
# for i in range(start_food):
#     bigmak.add_Food(random.randrange(1, rows) * dis, random.randrange(1, rows) * dis, 0, GREEN)

for snake in snakes.list:
    for i in range(start_length):
        snake.add_Cube()
def snake_loop1():
    global counter_gnil
    global counter_delete
    global counter_food
    global d
    if counter_gnil <= counter_gnil_max:
        counter_gnil += 1

    else:
        rand = random.randint(0, len(bigmak.list) - 1)
        bigmak.list[rand].typ = 1
        bigmak.list[rand].gniloy()
        counter_gnil = 0

    if counter_delete <= counter_delete_max:
        counter_delete += 1

    else:
        rand = random.randint(0, len(bigmak.list) - 1)
        bigmak.list.pop(rand)
        counter_delete = 0

    if counter_food <= counter_food_max:
        counter_food += 1

    else:
        bigmak.add_Food(random.randint(1, rows) * dis, random.randint(1, rows) * dis, 0, (255, 255, 255))
        counter_food = 0
    pygame.display.update()
    clock.tick(fps)
    screen.fill(pygame.Color('#0F003F'))

    for event in pygame.event.get():  # изменение направления и приращение попы на пробел
        if event.type == pygame.KEYDOWN:
            for snake in snakes.list:
                snake.re_dir(event)
            if event.key == pygame.K_SPACE:
                for snake in snakes.list:
                    snake.add_Cube()
            if event.key == pygame.K_ESCAPE:
                sn1_running.setter(False)
                menu.menu_running.setter(True)
        if event.type == pygame.QUIT:
            exit()
        
    keys = pygame.key.get_pressed()

    # if keys[pygame.K_SPACE]:
    #     for snake in snakes.list:
    #         snake.add_Cube()
    for food in bigmak.list:
        for snake in snakes.list:
            food.eat(snake)
    bigmak.draw(screen, dis)
    # f.draw(screen, dis)  # отрисовка еды
    # f.eat(s.body[len(s.body) - 1].pos[0], s.body[len(s.body) - 1].pos[1])  # проверка на съедение
    # f.eat1(s1.body[len(s1.body) - 1].pos[0], s1.body[len(s1.body) - 1].pos[1])

    for snake in snakes.list:
        snake.uyebalsya(snake.body[len(snake.body) - 1].pos)
        if snake.poison:
            snake.delete_Cube()
            d -= 1
        if len(snake.body) == 1 or d == 0:
            snake.poison = False
    snakes.move()

    snakes.draw()
    draw_grid(w, rows, screen)