import pygame as pg
import classes as cl
import snake as sn
import constants as const
import Varriables 
import slitherio as sl

width, height = const.WIDTH, const.WIDTH       # Screen's width and height
background_color = const.CYAN
pg.init()
pg.display.init()

screen = pg.display.set_mode((width, height))
screen.fill(background_color)
pg.display.flip()

menu_running = cl.BullVariables(True)
levelmenu_running=cl.BullVariables(False)

snake_text = cl.Button (const.TEXTX, const.WIDTH/2-225, const.TEXTH, const.TEXTH,'Snake', const.RED)
play_button = cl.Button(const.TEXTX, const.WIDTH/2-150, const.TEXTH, const.TEXTH,'Play', const.WHITE)
regime_button = cl.Button(const.TEXTX, const.WIDTH/2-100, const.TEXTH, const.TEXTH,'Regime', const.WHITE)
options_button = cl.Button (const.TEXTX, const.WIDTH/2-50, const.TEXTH, const.TEXTH, 'Options', const.WHITE)
credits_button = cl.Button(const.TEXTX, const.WIDTH/2 , const.TEXTH , const.TEXTH, 'Credits', const.WHITE)
score_button = cl.Button(const.TEXTX, const.WIDTH/2+50 , const.TEXTH , const.TEXTH, 'Score', const.WHITE)
quit_button = cl.Button(const.TEXTX, const.WIDTH/2+100 , const.TEXTH , const.TEXTH, 'Score', const.WHITE)

Torus_button = cl.Button(const.TEXTX, const.WIDTH/2-100 , const.TEXTH , const.TEXTH, 'Torus', const.WHITE)
Wall_button = cl.Button(const.TEXTX, const.WIDTH/2-50 , const.TEXTH , const.TEXTH, 'Wall', const.WHITE)
PVP_button = cl.Button(const.TEXTX, const.WIDTH/2 , const.TEXTH , const.TEXTH, 'PVP', const.WHITE)


def menu(running):
    screen.fill(const.CYAN)
    #print(menu_running)
    snake_text.write_text_on_button(screen)
    play_button.write_text_on_button(screen)
    quit_button.write_text_on_button(screen)
    regime_button.write_text_on_button(screen)
    options_button.write_text_on_button(screen)
    credits_button.write_text_on_button(screen)
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
                if Varriables.lev == 2:
                    menu_running.setter(False)
                    sl.sn1_running.setter(True)
                if Varriables.lev == 3:
                    menu_running.setter(False)
                    PVP.sn2_running.setter(True)
            if regime_button.is_click(event):
                menu_running.setter(False)
                levelmenu_running.setter(True)


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
            if event.key == pg.K_BACKSPACE:
                levelmenu_running.setter(False)
                menu_running.setter(True)

        







