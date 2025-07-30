import pygame as py
import game_state as GS
#hi
py.init()
clock = py.time.Clock()
running = True
height = 720
width = 720
gap = 84
size = 7
square_side = 80
cursor_pos = [0, 0]  # [row, col]
row, col = cursor_pos
font = py.font.SysFont('Verdana', 33)
screen = py.display.set_mode((width, height))
py.display.set_icon(py.image.load('./icon.png'))
game_state = [[0 for i in range(size)] for i in range(size)]

def draw_rect(id, rows, cols, cx, cy):
    positionY=rows*gap+cx+gap/2
    positionX=cols*gap+cy+gap/2
    def draw_text(text, color = (0, 0, 0)):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(positionY + square_side // 2, positionX + square_side // 2))
        screen.blit(text_surface, text_rect)
    properties = (positionY, positionX, square_side, square_side)
    if id == 0:
        py.draw.rect(screen, "#798394", properties, border_top_left_radius=20, border_bottom_right_radius=20) 
    elif id == 1:
        py.draw.rect(screen, "#FED3C9", properties, border_radius=15)
        draw_text('1')
    elif id == 2:
        py.draw.rect(screen, "#FCBDB7", properties, border_radius=15)
        draw_text('2')
    elif id == 3:
        py.draw.rect(screen, "yellow", properties, border_radius=18)
        draw_text('3')
    elif id == 4:
        py.draw.rect(screen, "green", properties, border_radius=18)
        draw_text('4')
    elif id == 5:
        py.draw.rect(screen, "pink", properties, border_radius=18)
        draw_text('5')
    elif id == 6:
        py.draw.rect(screen, "salmon", properties, border_radius=18)
        draw_text('6')
    elif id == 7:
        py.draw.rect(screen, "#B5333C", properties, border_radius=18)
        draw_text('7', (255, 255, 255))
    else:
        py.draw.rect(screen, "beige", properties)
        draw_text(str(id))

def draw():
    screen.fill("white")
    diff = gap-square_side
    grid_width = size*square_side+4*diff+gap
    grid_height = size*square_side+4*diff+gap
    cx = (width - grid_width)//2
    cy = (height - grid_height)//2
        #draw square underlay
    py.draw.rect(screen, "#96a0b0", (cx, cy, grid_width, grid_height), border_radius=15)
        #draw sizexsize grid of squares
    for rows in range(size):
            for cols in range(size):
                draw_rect(game_state[rows][cols], cols, rows, cx, cy)

def chain_loop():
    # Create a copy of the current state
    last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
    def has_changed():
        return any(game_state[row][col] != last_state[row][col] for row in range(size) for col in range(size))
    first = 0
    # Keep track of changes
    changed = True
    while changed:
        changed = False
        
        # Check if state changed after each operation
        GS.fill_game_state(game_state, size)
        if has_changed():
            changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        draw()
        py.display.flip()
        clock.tick(first)
        
        GS.check_and_merge(game_state, size)
        if has_changed():
            changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        draw()
        py.display.flip()
        clock.tick(first)
        
        GS.gravity(game_state, size)
        if has_changed():
            changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        draw()
        py.display.flip()
        clock.tick(first)
        first = 1; #keep speed when the grid is filled and no merges

while running:   
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    # INSERT_YOUR_CODE
    # WASD movement and selection
    
    

    if event.type == py.KEYDOWN:
        if event.key == py.K_w:
            row = (row - 1) % size
        elif event.key == py.K_s:
            row = (row + 1) % size
        elif event.key == py.K_a:
            col = (col - 1) % size
        elif event.key == py.K_d:
            col = (col + 1) % size
        cursor_pos = [row, col]

    # Optionally, you can highlight the selected square in your draw() function
    chain_loop()
    
py.quit()
print("done")