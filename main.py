import menu
import snake as sn
import classes as cl

running = cl.BullVariables(True)

while running.getter():
    if menu.menu_running.getter():
        menu.menu(running)
    if sn.sn_running.getter():
        sn.snake_loop()
