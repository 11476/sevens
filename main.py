from ast import match_case
import pygame as py
#hi
py.init()

clock = py.time.Clock()
running = True
height = 720
width = 720
gap = 120
square_side = 100
screen = py.display.set_mode((width, height))
game_state = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 21, 63],
    [189, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]]
def draw_rect(id, rows, cols, cx, cy):
    positionY=rows*gap+cx+gap/2
    positionX=cols*gap+cy+gap/2
    def draw_text(text):
        font = py.font.SysFont(None, 48)
        text_surface = font.render(text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(positionY + square_side // 2, positionX + square_side // 2))
        screen.blit(text_surface, text_rect)
    properties = (positionY, positionX, square_side, square_side)
    match id:
        case 0:
            py.draw.rect(screen, "gray", properties, border_top_left_radius=20, border_bottom_right_radius=20) 
        case 1:
            py.draw.rect(screen, "#FED3C9", properties, border_radius=15)
            draw_text('1') 
        case 2:
            py.draw.rect(screen, "#FCBDB7", properties, border_radius=15)
            draw_text('2') 
        case 3:
            py.draw.rect(screen, "#FBA7A5", properties, border_radius=18)
            draw_text('3') 
        case 4:
            py.draw.rect(screen, "#FA9193", properties, border_radius=18)
            draw_text('4') 
        case 5:
            py.draw.rect(screen, "#F87B81", properties, border_radius=18)
            draw_text('5') 
        case _:
            py.draw.rect(screen, "beige", properties)
            draw_text(str(id)) 
            
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    screen.fill("white")
    diff = gap-square_side
    grid_width = 5*square_side+4*diff+gap
    grid_height = 5*square_side+4*diff+gap
    cx = (width - grid_width)//2
    cy = (height - grid_height)//2
    #draw square underlay
    py.draw.rect(screen, "#96a0b0", (cx, cy, grid_width, grid_height), border_radius=15)
    #draw 5x5 grid of squares
    for rows in range(5):
        for cols in range(5):
            draw_rect(game_state[rows][cols], cols, rows, cx, cy)
            
    
    py.display.flip()
    py.display.set_icon(screen)
    clock.tick(31)

py.quit()
print("done")