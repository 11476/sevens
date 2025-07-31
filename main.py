from math import sqrt
import pygame as py
import game_state as GS
#hi
py.init()
state_speed = 0 #For better loading at first, and also being able to see the "animations" after
state_changed = True
clock = py.time.Clock()
running = True
height = 720
width = 720
gap = 64
size = 10
square_side = 60
cursor_pos = None  # [row, col]
locked_cursor_pos = None  # [row, col]
row, col = 0, 0
font = py.font.SysFont('Verdana', 33)
<<<<<<< HEAD
fontBold = py.font.SysFont('Verdana', 33, bold=True, italic=True )
=======
fontBold = py.font.SysFont('Verdana', 33, True, True)
>>>>>>> main
screen = py.display.set_mode((width, height))
py.display.set_icon(py.image.load('./icon.png'))
game_state = [[0 for i in range(size)] for i in range(size)]

<<<<<<< HEAD
def draw_rect(id, rows, cols):
    positionY=rows*gap+gap/2
    positionX=cols*gap+gap/2
    def draw_text(text, color = (0, 0, 0), bold=False):
=======
def draw_rect(id, rows, cols, cx, cy):
    positionY=rows*gap+cx+gap/2
    positionX=cols*gap+cy+gap/2
    def draw_text(text, color = (0, 0, 0), bold = False):
>>>>>>> main
        if bold: text_surface = fontBold.render(text, True, color)
        else: text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(positionY + square_side // 2, positionX + square_side // 2))
        screen.blit(text_surface, text_rect)
    properties = (positionY, positionX, square_side, square_side)
    if id == 0:
        py.draw.rect(screen, "#798394", properties, border_top_left_radius=20, border_bottom_right_radius=20) 
    elif id == 1:
        py.draw.rect(screen, "#FED3C9", properties, border_radius=18)
        draw_text('1')
    elif id == 2:
        py.draw.rect(screen, "#FCBDB7", properties, border_radius=18)
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
        draw_text('7', (255, 255, 255), True)
    else:
<<<<<<< HEAD
        py.draw.rect(screen, "beige", properties, border_radius=3)
        draw_text(str(id))
=======
        py.draw.rect(screen, "beige", properties)
        draw_text(str(id), bold=True)
>>>>>>> main

def draw(loading = False):
    screen.fill("white")
    if loading:
        print(loading)
        positionY = width // 2 - square_side // 2
        positionX = height // 2 - square_side // 2
        text_surface = font.render('Loading...', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(positionY + square_side // 2, positionX + square_side // 2))
        screen.blit(text_surface, text_rect)
        return
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
                draw_rect(game_state[rows][cols], cols, rows)

def chain_loop():
    global state_changed, state_speed
    # Create a copy of the current state
    last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
    def has_state_changed():
        return any(game_state[row][col] != last_state[row][col] for row in range(size) for col in range(size))

    # Keep track of changes
    while state_changed:
        if game_state == last_state:
            state_changed = False
        # Check if state changed after each operation
        GS.fill_game_state(game_state, size)
        if has_state_changed():
            state_changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        draw()
#        py.display.flip()
        clock.tick(state_speed)
        
        GS.check_and_merge(game_state, size)
        if has_state_changed():
            state_changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        draw()
#        py.display.flip()
        clock.tick(state_speed)
        
        GS.gravity(game_state, size)
        if has_state_changed():
            state_changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        draw()
#        py.display.flip()
        clock.tick(state_speed)
    state_speed = 1
# draw(loading=True)
# py.display.flip()
while running:   
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                row = (row - 1) % size
            elif event.key == py.K_s:
                row = (row + 1) % size
            elif event.key == py.K_a:
                col = (col - 1) % size
            elif event.key == py.K_d:
                col = (col + 1) % size
            elif event.key == py.K_SPACE:
                locked_cursor_pos = [row, col]
            cursor_pos = [row, col]
    
    
    chain_loop()
    draw()
    if cursor_pos:
        highlight_color = (0, 255, 0)  # bright green
        highlight_thickness = 5
        highlight_rect = (
            cursor_pos[1] * gap + gap // 2,
            cursor_pos[0] * gap + gap // 2,
            square_side, square_side
        )
        py.draw.rect(screen, highlight_color, highlight_rect, highlight_thickness, border_radius=18)
    if locked_cursor_pos:
        highlight_color = (255, 120, 0)  # bright green
        highlight_thickness = 8
        highlight_rect = (
            locked_cursor_pos[1] * gap + gap // 2,
            locked_cursor_pos[0] * gap + gap // 2,
            square_side, square_side
        )
        py.draw.rect(screen, highlight_color, highlight_rect, highlight_thickness, border_radius=18)
    py.display.flip()
    clock.tick(31)
py.quit()
print("done")