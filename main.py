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
    # center at the center of the screen, not top-left of grid
    grid_width = 5 * 100 + 4 * 20  # 5 squares, 4 gaps of 20px (120-100)
    grid_height = 5 * 100 + 4 * 20
    cx = (width - grid_width) // 2
    cy = (height - grid_height) // 2
    # draw 5x5 square of rectangles
    for i in range(5):
        for j in range(5):
            py.draw.rect(screen, "#798394", (i*120+cx, j*120+cy, 100, 100)) 
    py.display.flip()
    clock.tick(60)
py.quit()
print("done")