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
font = py.font.SysFont('Verdana', 33)
screen = py.display.set_mode((width, height))
py.display.set_icon(py.image.load('./icon.png'))
game_state = [[0 for i in range(size)] for i in range(size)]
last_game_state = [[0 for i in range(size)] for i in range(size)]

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
        clock.tick(1)
        
        GS.check_and_merge(game_state, size)
        if any(game_state[row][col] != last_state[row][col] for row in range(size) for col in range(size)):
            changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        draw()
        py.display.flip()
        clock.tick(1)
        
        GS.gravity(game_state, size)
        if any(game_state[row][col] != last_state[row][col] for row in range(size) for col in range(size)):
            changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        draw()
        py.display.flip()
        clock.tick(1)

while running:   
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    # Detect clicks on a square
    if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
        mouse_x, mouse_y = event.pos
        # Calculate grid's top-left corner
        grid_width = size * 60 + (size - 1) * 8
        grid_height = size * 60 + (size - 1) * 8
        cx = (width - grid_width)//2
        cy = (height - grid_height)//2
        # Check if click is inside the grid
        if cx <= mouse_x < cx + grid_width and cy <= mouse_y < cy + grid_height:
            # Calculate which square was clicked
            rel_x = mouse_x - cx
            rel_y = mouse_y - cy
            for row in range(size):
                for col in range(size):
                    square_x = col * (60 + 8)
                    square_y = row * (60 + 8)
                    if (square_x <= rel_x < square_x + 60) and (square_y <= rel_y < square_y + 60):
                        # You can handle the click on (row, col) here
                        print(f"Clicked on square: row={row}, col={col}")
                        # For example, you could set a flag or call a function
                        break
    chain_loop()
    
py.quit()
print("done")