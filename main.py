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
    if sn.sn_running.getter():
        sn.snake_loop()
    if sl.sn1_running.getter():
        sl.snake_loop1()
    #if sl.sn1_running.getter():
