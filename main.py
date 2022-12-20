import menu
import snake as sn
import classes as cl
import slitherio as sl
running = cl.BullVariables(True)

while running.getter():
    if menu.menu_running.getter():
        menu.menu(running)
    elif menu.levelmenu_running.getter():
        menu.levelmenu(running)
    elif menu.optionsmenu_running.getter():
        menu.optionsmenu(running)
    elif menu.difficultmenu_running.getter():
        menu.difficultmenu(running)
    elif menu.helpmenu_running.getter():
        menu.helpmenu(running)
    elif menu.help1menu_running.getter():
        menu.help1menu(running)
    elif menu.help2menu_running.getter():
        menu.help2menu(running)
    elif menu.help3menu_running.getter():
        menu.help3menu(running)
    if sn.sn_running.getter():
        sn.snake_loop()
    if sl.sn1_running.getter():
        sl.snake_loop1()
    #if sl.sn1_running.getter():
