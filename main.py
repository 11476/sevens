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
    screen.fill("white")
    # center
    cx = width/2 - 250
    cy = height/2 - 250
    # draw 5x5 square of rectangles
    for i in range(5):
        for j in range(5):
            py.draw.rect(screen, "black", (i*120+cx, j*120+cy, 100, 100)) 
    py.display.flip()
    clock.tick(60)
py.quit()
print("done")