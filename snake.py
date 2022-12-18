import pygame
import random 
import pygame

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
    def __init__(self):
        dis = w // rows
        self.head_surf = pygame.Surface((dis, dis))
        self.head_surf.fill((0, 0, 255))
        self.head_rect = self.head_surf.get_rect(topleft=(w / 2, (h / 2)-dis/2))
        self.pos = [self.head_rect.left, self.head_rect.top]
        self.vx = dis
        self.vy = 0

    # def blit_screen(self):
    #     self.game.window.blit(self.game.display, (0, 0))

    def move(self):
        self.pos = [self.pos[0] + self.vx, self.pos[1] + self.vy]
        self.head_rect = self.head_surf.get_rect(topleft=self.pos)
        if self.head_rect.left >= 800:
            self.pos = [-dis, self.pos[1] + self.vy]
        screen.blit(self.head_surf, self.head_rect)

def draw_grid(w, rows, surface):
    size_btwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(surface, (100, 100, 100), (x, 0), (x, w))
        pygame.draw.line(surface, (100, 100, 100), (0, y), (w, y))

c = Cube()

while sn_running:
    pygame.display.update()
    clock.tick(fps)
    screen.fill((0, 0, 0))
    draw_grid(w, rows, screen)
    c.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

#
