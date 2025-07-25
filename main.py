import pygame as py
#hi
py.init()

clock = py.time.Clock()
running = True
height = 720
width = 1280
screen = py.display.set_mode((width, height))
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    screen.fill("purple")

    py.display.flip()
    clock.tick(31)
py.quit()
print("done")