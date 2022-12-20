import pygame as pg
import classes as cl
import snake as sn
import constants as const
import Varriables 
import slitherio as sl


sn.leader_score.sort()
sn.leader_score.reverse()

phon = pg.image.load('Abubs.jpg')
width, height = const.WIDTH, const.WIDTH       # Screen's width and height
background_color = const.CYAN
pg.init()
pg.display.init()
screen = pg.display.set_mode((width, height))
screen.fill(background_color)
pg.display.flip()
screen.blit(phon, (0, 0))

menu_running = cl.BullVariables(True)
levelmenu_running=cl.BullVariables(False)
optionsmenu_running=cl.BullVariables(False)
difficultmenu_running=cl.BullVariables(False)
helpmenu_running=cl.BullVariables(False)
helpmenu_running = cl.BullVariables(False)
help1menu_running = cl.BullVariables(False)
help2menu_running = cl.BullVariables(False)
help3menu_running = cl.BullVariables(False)
help4menu_running = cl.BullVariables(False)
scoremenu_running = cl.BullVariables(False)

snake_text = cl.Button (const.TEXTX, const.WIDTH/2-225, const.TEXTH, const.TEXTH,'Snake', const.RED)
play_button = cl.Button(const.TEXTX, const.WIDTH/2-150, const.TEXTH+60, const.TEXTH,'Play', const.WHITE)
regime_button = cl.Button(const.TEXTX, const.WIDTH/2-100, const.TEXTH+60, const.TEXTH,'Regime', const.WHITE)
options_button = cl.Button (const.TEXTX, const.WIDTH/2-50, const.TEXTH+60, const.TEXTH, 'Options', const.WHITE)
score_button = cl.Button(const.TEXTX, const.WIDTH/2 , const.TEXTH+60, const.TEXTH, 'Score', const.WHITE)
quit_button = cl.Button(const.TEXTX, const.WIDTH/2+50 , const.TEXTH+60, const.TEXTH, 'Quit', const.WHITE)

Torus_button = cl.Button(const.TEXTX+20, const.WIDTH/2-100 , const.TEXTH+60, const.TEXTH, 'Torus', const.WHITE)
Wall_button = cl.Button(const.TEXTX+20, const.WIDTH/2-50 , const.TEXTH+60, const.TEXTH, 'Wall', const.WHITE)
PVP_button = cl.Button(const.TEXTX+20, const.WIDTH/2 , const.TEXTH+60, const.TEXTH, 'PVP', const.WHITE)

Difficult_button = cl.Button(const.TEXTX, const.WIDTH/2-100, const.TEXTH+60, const.TEXTH, 'Speed', const.WHITE)
Help_button = cl.Button(const.TEXTX, const.WIDTH/2-50 , const.TEXTH+60, const.TEXTH, 'Help', const.WHITE)

dif1_button = cl.Button(const.TEXTX, const.WIDTH/2-120 , const.TEXTH+60, const.TEXTH, 'Speed 1', const.WHITE)
dif2_button = cl.Button(const.TEXTX, const.WIDTH/2-70 , const.TEXTH+60, const.TEXTH, 'Speed 2', const.WHITE)
dif3_button = cl.Button(const.TEXTX, const.WIDTH/2-20 , const.TEXTH+60, const.TEXTH, 'Speed 3', const.WHITE)
dif4_button = cl.Button(const.TEXTX, const.WIDTH/2+30 , const.TEXTH+60, const.TEXTH, 'Speed 4', const.WHITE)
dif5_button = cl.Button(const.TEXTX, const.WIDTH/2+80 , const.TEXTH+60, const.TEXTH, 'Speed 5', const.WHITE)

help1_button = cl.Button(const.TEXTX-20, const.WIDTH/2-120 , const.TEXTH+120, const.TEXTH, 'About Torus', const.WHITE)
help2_button = cl.Button(const.TEXTX-20, const.WIDTH/2-70 , const.TEXTH+120, const.TEXTH, 'About Wall', const.WHITE)
help3_button = cl.Button(const.TEXTX-20, const.WIDTH/2-20 , const.TEXTH+120, const.TEXTH, 'About PVP', const.WHITE)
help4_button = cl.Button(const.TEXTX-20, const.WIDTH/2+30 , const.TEXTH+60, const.TEXTH, 'Authors', const.WHITE)

rez1_button =cl.Button(190, const.WIDTH/2-70 , const.TEXTH , const.TEXTH, 'First result:' + str(sn.leader_score[0]), const.WHITE)
rez2_button =cl.Button(190, const.WIDTH/2-40 , const.TEXTH , const.TEXTH, 'Second result:' + str(sn.leader_score[1]), const.WHITE)
rez3_button =cl.Button(190, const.WIDTH/2-10 , const.TEXTH , const.TEXTH, 'Third result:' + str(sn.leader_score[2]), const.WHITE)

def menu(running):
    screen.fill(const.CYAN)
    #print(menu_running)
    screen.blit(phon, (0, 0))
    snake_text.write_text_on_button(screen)
    play_button.write_text_on_button(screen)
    quit_button.write_text_on_button(screen)
    regime_button.write_text_on_button(screen)
    options_button.write_text_on_button(screen)
    score_button.write_text_on_button(screen)

    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            menu_running.setter(False)
            running.setter(False)
        if event.type == pg.MOUSEBUTTONDOWN:
            if quit_button.is_click(event):
                menu_running.setter(False)
                running.setter(False)
            if play_button.is_click(event):
                if Varriables.lev == 1:
                    menu_running.setter(False)
                    sn.sn_running.setter(True)
                elif Varriables.lev == 2:
                    menu_running.setter(False)
                    #sl.sn2_running.setter(True)
                elif Varriables.lev == 3:
                    menu_running.setter(False)
                    sl.sn1_running.setter(True)
            if regime_button.is_click(event):
                menu_running.setter(False)
                levelmenu_running.setter(True)
            if options_button.is_click(event):
                menu_running.setter(False)
                optionsmenu_running.setter(True)
            if score_button.is_click(event):
                menu_running.setter(False)
                scoremenu_running.setter(True)



def levelmenu(running):
    screen.fill(const.CYAN)
    Torus_button.write_text_on_button(screen)
    Wall_button.write_text_on_button(screen)
    PVP_button.write_text_on_button(screen)
    pg.display.update()
    for event in pg.event.get():
         if event.type == pg.QUIT:
            levelmenu_running.setter(False)
            running.setter(False)
         if event.type == pg.MOUSEBUTTONDOWN:
            if Torus_button.is_click(event):
                levelmenu_running.setter(False)
                menu_running.setter(True)
                Varriables.lev=1
         if event.type == pg.MOUSEBUTTONDOWN:
            if Wall_button.is_click(event):
                levelmenu_running.setter(False)
                menu_running.setter(True)
                Varriables.lev=2
         if event.type == pg.MOUSEBUTTONDOWN:
            if PVP_button.is_click(event):
                levelmenu_running.setter(False)
                menu_running.setter(True)
                Varriables.lev=3
         if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                levelmenu_running.setter(False)
                menu_running.setter(True)

def optionsmenu(running):
    screen.fill(const.CYAN)
    Difficult_button.write_text_on_button(screen)
    Help_button.write_text_on_button(screen)
    pg.display.update()
    for event in pg.event.get():
         if event.type == pg.QUIT:
            optionsmenu_running.setter(False)
            running.setter(False)
         if event.type == pg.MOUSEBUTTONDOWN:
            if Difficult_button.is_click(event):
                optionsmenu_running.setter(False)
                difficultmenu_running.setter(True)
         if event.type == pg.MOUSEBUTTONDOWN:
            if Help_button.is_click(event):
                optionsmenu_running.setter(False)
                helpmenu_running.setter(True)
         if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                optionsmenu_running.setter(False)
                menu_running.setter(True)

def difficultmenu(running):
    screen.fill(const.CYAN)
    dif1_button.write_text_on_button(screen)
    dif2_button.write_text_on_button(screen)
    dif3_button.write_text_on_button(screen)
    dif4_button.write_text_on_button(screen)
    dif5_button.write_text_on_button(screen)
    pg.display.update()
    for event in pg.event.get():
         if event.type == pg.QUIT:
            difficultmenu_running.setter(False)
            running.setter(False)
         if event.type == pg.MOUSEBUTTONDOWN:
            if dif1_button.is_click(event):
                difficultmenu_running.setter(False)
                optionsmenu_running.setter(True)
                const.FPS = 10
            if dif2_button.is_click(event):
                difficultmenu_running.setter(False)
                optionsmenu_running.setter(True)
                const.FPS = 12
            if dif3_button.is_click(event):
                difficultmenu_running.setter(False)
                optionsmenu_running.setter(True)
                const.FPS = 14
            if dif4_button.is_click(event):
                difficultmenu_running.setter(False)
                optionsmenu_running.setter(True)
                const.FPS = 16
            if dif5_button.is_click(event):
                difficultmenu_running.setter(False)
                optionsmenu_running.setter(True)
                const.FPS = 18
         if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                difficultmenu_running.setter(False)
                optionsmenu_running.setter(True)

def helpmenu(running):
    screen.fill(const.CYAN)
    help1_button.write_text_on_button(screen)
    help2_button.write_text_on_button(screen)
    help3_button.write_text_on_button(screen)
    help4_button.write_text_on_button(screen)
    pg.display.update()
    for event in pg.event.get():
         if event.type == pg.QUIT:
            helpmenu_running.setter(False)
            running.setter(False)
         if event.type == pg.MOUSEBUTTONDOWN:
            if help1_button.is_click(event):
                helpmenu_running.setter(False)
                help1menu_running.setter(True)
            if help2_button.is_click(event):
                helpmenu_running.setter(False)
                help2menu_running.setter(True)
            if help3_button.is_click(event):
                helpmenu_running.setter(False)
                help3menu_running.setter(True)
            if help4_button.is_click(event):
                helpmenu_running.setter(False)
                help4menu_running.setter(True)            
         if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                helpmenu_running.setter(False)
                optionsmenu_running.setter(True)

def help1menu(running):
    screen.fill(const.CYAN)
    screen.blit(const.text1, (80, const.WIDTH/2-100))
    pg.display.update()
    for event in pg.event.get():
         if event.type == pg.QUIT:
            help1menu_running.setter(False)
            running.setter(False)
         if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                help1menu_running.setter(False)
                helpmenu_running.setter(True)

def help2menu(running):
    screen.fill(const.CYAN)
    screen.blit(const.text2, (65, const.WIDTH/2-100))
    pg.display.update()
    for event in pg.event.get():
         if event.type == pg.QUIT:
            help2menu_running.setter(False)
            running.setter(False)
         if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                help2menu_running.setter(False)
                helpmenu_running.setter(True)

def help3menu(running):
    screen.fill(const.CYAN)
    screen.blit(const.text3, (70, const.WIDTH/2-100))
    help1_button.write_text_on_button(screen)
    help2_button.write_text_on_button(screen)
    help3_button.write_text_on_button(screen)
    pg.display.update()
    for event in pg.event.get():
         if event.type == pg.QUIT:
            help3menu_running.setter(False)
            running.setter(False)
         if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                help3menu_running.setter(False)
                helpmenu_running.setter(True)

def help4menu(running):
    screen.fill(const.CYAN)
    screen.blit(const.text4, (190, const.WIDTH/2-100+50))
    screen.blit(const.text5, (190, const.WIDTH/2-140+50))
    screen.blit(const.text6, (190, const.WIDTH/2-180+50))
    pg.display.update()
    for event in pg.event.get():
         if event.type == pg.QUIT:
            help4menu_running.setter(False)
            running.setter(False)
         if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                help4menu_running.setter(False)
                helpmenu_running.setter(True)

def scoremenu(running):
    screen.fill(const.CYAN)
    screen.blit(const.text7, (210, const.WIDTH/2-100))
    rez1_button.write_text_on_button(screen)
    rez2_button.write_text_on_button(screen)
    rez3_button.write_text_on_button(screen)
    pg.display.update()
    for event in pg.event.get():
         if event.type == pg.QUIT:
            help4menu_running.setter(False)
            running.setter(False)
         if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                scoremenu_running.setter(False)
                menu_running.setter(True)


              





        







