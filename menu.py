import pygame as pg
import classes as cl
import snake as sn
import constants as const

width, height = const.WIDTH, const.WIDTH       # Screen's width and height
background_color = const.CYAN
pg.init()
pg.display.init()

screen = pg.display.set_mode((width, height))
screen.fill(background_color)
pg.display.flip()
menu_running = cl.BullVariables(True)

snake_text = cl.Button (const.TEXTX, const.WIDTH/2-225, const.TEXTH, const.TEXTH,'Snake', const.RED)
play_button = cl.Button(const.TEXTX, const.WIDTH/2-150, const.TEXTH, const.TEXTH,'Play', const.WHITE)
level_button = cl.Button(const.TEXTX, const.WIDTH/2-100, const.TEXTH, const.TEXTH,'Level', const.WHITE)
options_button = cl.Button (const.TEXTX, const.WIDTH/2-50, const.TEXTH, const.TEXTH, 'Options', const.WHITE)
credits_button = cl.Button(const.TEXTX, const.WIDTH/2 , const.TEXTH , const.TEXTH, 'Credits', const.WHITE)
score_button = cl.Button(const.TEXTX, const.WIDTH/2+50 , const.TEXTH , const.TEXTH, 'Score', const.WHITE)
quit_button = cl.Button(const.TEXTX, const.WIDTH/2+100 , const.TEXTH , const.TEXTH, 'Score', const.WHITE)

#level1_button = cl.Button(250, 200, 30, 30,'Level')



def menu(running):
    #print(menu_running)
    snake_text.write_text_on_button(screen)
    play_button.write_text_on_button(screen)
    quit_button.write_text_on_button(screen)
    level_button.write_text_on_button(screen)
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
                menu_running.setter(False)
                sn.sn_running.setter(True)
            #if level_button.is_click(event):
#def levelmenu(running):


