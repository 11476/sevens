import pygame as py
#hi
py.init()
screen = py.display.set_mode((1280, 720))
clock = py.time.Clock()
running = True

while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    py.display.flip()
    clock.tick(31)
py.quit()