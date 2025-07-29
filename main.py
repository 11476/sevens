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
diff = gap-square_side
grid_width = size*square_side+4*diff+gap
grid_height = size*square_side+4*diff+gap
cx = (width - grid_width)//2
cy = (height - grid_height)//2

font = py.font.SysFont('Verdana', 33)
Bfont = py.font.SysFont('Verdana', 33, True, True)
screen = py.display.set_mode((width, height))
py.display.set_icon(py.image.load('./icon.png'))
game_state = [[0 for i in range(size)] for i in range(size)]
last_game_state = [[0 for i in range(size)] for i in range(size)]

def draw_rect(id, rows, cols, cx, cy):
    positionY=rows*gap+cx+gap/2
    positionX=cols*gap+cy+gap/2
    def draw_text(text, color = (0, 0, 0), bold=False):
        if bold: text_surface = font.render(text, True, color)
        else: text_surface = Bfont.render(text, True, color)
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
        draw_text(str(id), bold=True)

def draw():
    screen.fill("white")
    py.draw.rect(screen, "#96a0b0", (cx, cy, grid_width, grid_height), border_radius=15)
        #draw sizexsize grid of squares
    for rows in range(size):
            for cols in range(size):
                draw_rect(game_state[rows][cols], cols, rows, cx, cy)

def chain_loop():
    # Create a copy of the current state
    last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
    
    # Keep track of changes
    changed = True
    while changed:
        changed = False
        
        # Check if state changed after each operation
        GS.fill_game_state(game_state, size)
        if any(game_state[row][col] != last_state[row][col] for row in range(size) for col in range(size)):
            changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        draw()
        py.display.flip()
        clock.tick(4)
        
        GS.check_and_merge(game_state, size)
        if any(game_state[row][col] != last_state[row][col] for row in range(size) for col in range(size)):
            changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        draw()
        py.display.flip()
        clock.tick(4)
        
        GS.gravity(game_state, size)
        if any(game_state[row][col] != last_state[row][col] for row in range(size) for col in range(size)):
            changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        draw()
        py.display.flip()
        clock.tick(2)

while running:   
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

# Add ability to swap two cells with mouse clicks
selected_cell = None  # Store the first selected cell

def get_cell_from_mouse(pos, cx, cy):
    mx, my = pos
    # Check if click is inside the grid
    if cx <= mx < cx + size * gap and cy <= my < cy + size * gap:
        col = (mx - cx) // gap
        row = (my - cy) // gap
        if 0 <= row < size and 0 <= col < size:
            return int(row), int(col)
    return None

while running:   
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    chain_loop()
    
py.quit()
print("done")