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
play_button = cl.Button(250, 150, const.number_size, const.number_size,'Play')
level_button = cl.Button(250, 200, const.number_size, const.number_size,'Level')
options_button = cl.Button (250, 250, const.number_size, const.number_size, 'Options')
credits_button = cl.Button(250, 250, const.number_size , const.number_size, 'Credits')

quit_button = cl.Button(250, 300, const.number_size, const.number_size, 'Quit')

level1_button = cl.Button(250, 200, const.number_size, const.number_size,'Level')



def menu(running):
    #print(menu_running)
    play_button.write_text_on_button(screen)
    quit_button.write_text_on_button(screen)
    level_button.write_text_on_button(screen)
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


