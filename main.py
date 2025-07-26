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
    # center at the center of the screen, not top-left of grid
    grid_width = 5 * 100 + 4 * 20  
    grid_height = 5 * 100 + 4 * 20
    cx = (width - grid_width) // 2+gap
    cy = (height - grid_height) // 2+gap
    #draw square underlay
    py.draw.rect(screen, "#96a0b0", (cx, cy, grid_width, grid_height), border_radius=15)
    # draw 5x5 square of rectangles
   
    for i in range(5):
        for j in range(5):
            py.draw.rect(screen, "#798394", (i*gap+cx, j*gap+cy, square_side, square_side), border_top_left_radius=20) 
    py.display.flip()
    py.display.set_caption(str(clock.get_fps()))
    clock.tick(60)

py.quit()
print("done")