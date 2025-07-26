import pygame as py
#hi
py.init()

clock = py.time.Clock()
running = True
height = 720
width = 1280
gap = 120
square_side = 100
screen = py.display.set_mode((width, height))
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    screen.fill("white")
    grid_width = 5*100+4*20+gap
    grid_height = 5*100+4*20+gap
    cx = (width - grid_width)//2
    cy = (height - grid_height)//2
    py.draw.rect(screen, "#96a0b0", (cx, cy, grid_width, grid_height), border_radius=15)
    for i in range(5):
        for j in range(5):
            #center squares
            py.draw.rect(screen, "#798394", (i*gap+cx+gap/2, j*gap+cy+gap/2, square_side, square_side), border_top_left_radius=20) 
    py.display.flip()
    py.display.set_caption(str(clock.get_fps()))
    py.display.set_icon(screen)
    clock.tick(31)

py.quit()
print("done")