import pygame
import random
import pygame

dir = [1, 0]
w = 800
h = 600
rows = 20
dis = w // rows
pygame.init()
sn_running = True
screen = pygame.display.set_mode((800, 600))
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()
fps = 5


# head_surf = pygame.Surface((50, 50))
# head_rect = head_surf.get_rect(midbottom=(400, 300))
# head_surf.fill((0, 0, 255))
# screen.blit(head_surf, head_rect)
# while sn_running:
#     pygame.display.update()
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit()
###
class Cube:
    def __init__(self, pos):
        self.pos = pos
        self.surf = pygame.Surface((dis, dis))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect(topleft=pos)
        self.pos = [self.rect.left, self.rect.top]

        # self.vx = dis
        # self.vy = 0

    # def blit_screen(self):
    #     self.game.window.blit(self.game.display, (0, 0))
cube1 = Cube([0,0])

class Snake:
    def __init__(self):
        self.body = [cube1]
        self.head = self.body[len(self.body)-1]
        self.tail = self.body[0]

    def add_Cube(self, pos):
        self.body.append(0)
        self.head = self.body[len(self.body)-1]
        self.head = Cube(pos)

    def move(self):
        self.tail.pos = [self.head.pos[0] + dir[0]*dis, self.head.pos[1] + dir[1]*dis]
        if self.head.pos[0] >= w:
            self.head.pos[0] = 0
        if self.head.pos[0] <= -dis:
            self.head.pos[0] = w-dis
        if self.head.pos[1] >= h:
            self.head.pos[1] = 0
        if self.head.pos[1] <= -dis:
            self.head.pos[1] = w-dis

    def draw(self):
        for i in self.body:
            i.surf = pygame.Surface((dis, dis))
            i.surf.fill((0, 0, 255))
            i.rect = i.surf.get_rect(topleft=i.pos)
            screen.blit(i.surf, i.rect)


def draw_grid(w, rows, surface):
    size_btwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(surface, (100, 100, 100), (x, 0), (x, w))
        pygame.draw.line(surface, (100, 100, 100), (0, y), (w, y))


def re_dir():
    global dir
    for i in pygame.event.get():
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_UP and dir != [0, 1]:
                dir = [0, -1]
            if i.key == pygame.K_DOWN and dir != [0, -1]:
                dir = [0, 1]
            if i.key == pygame.K_LEFT and dir != [1, 0]:
                dir = [-1, 0]
            if i.key == pygame.K_RIGHT and dir != [-1, 0]:
                dir = [1, 0]

s = Snake()


while sn_running:
    pygame.display.update()
    clock.tick(fps)
    screen.fill((0, 0, 0))
    draw_grid(w, rows, screen)
    re_dir()
    s.move()
    s.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

#
