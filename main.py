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
    screen.fill("beige")
    # draw 5x5 square of rectangles
    for i in range(5):
        for j in range(5):
            py.draw.rect(screen, "black", (i*200, j*200, 200, 200)) 
    py.display.flip()
    clock.tick(31)
py.quit()
print("done")