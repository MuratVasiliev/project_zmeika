import pygame as pg
import classes as cl
import snake as sn
import constants as const

width, height = const.WIDTH, const.WIDTH       # Screen's width and height
background_color = (0, 0, 0)
pg.init()
pg.display.init()

screen = pg.display.set_mode((width, height))
screen.fill(background_color)
pg.display.flip()
menu_running = cl.BullVariables(True)
play_button = cl.Button(100,100,70,30,'play')
quit_button = cl.Button(100,200,70,30,'quit')



def menu(running):
    #print(menu_running)
    play_button.write_text_on_button(screen)
    quit_button.write_text_on_button(screen)
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