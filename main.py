from math import sqrt
import random
import pygame as py
import game_state as GS
#hi
py.init()
state_speed = 8 
state_changed = True
clock = py.time.Clock()
running = True
height = 720
width = 720
score_width = 200
gap = 64
size = 10
square_side = 60
cursor_pos = None  # [row, col]
locked_cursor_pos = None  # [row, col]
row, col = None, None
font = py.font.SysFont('Verdana', 20)
fontBold = py.font.SysFont('Verdana', 30, bold=True, italic=True)
screen = py.display.set_mode((width+score_width, height))
py.display.set_icon(py.image.load('./icon.png'))
game_state = [[0 for i in range(size)] for i in range(size)]
grid_width = size * square_side + (size-1) * 4
grid_height = size * square_side + (size-1) * 4
score = 0
moves = 25

def draw_rect(id, rows, cols):
    # Calculate the Y position to center the square underlay for the given row
    positionY = rows * gap + (height - grid_height)//2
    # Calculate the X position to center the square underlay for the given column
    positionX = cols * gap + (width - grid_width)//2
    def draw_text(text, color = (0, 0, 0), bold=False):
        if bold: text_surface = fontBold.render(text, True, color)
        else: text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(positionY + square_side // 2, positionX + square_side // 2))
        screen.blit(text_surface, text_rect)
    properties = (positionY, positionX, square_side, square_side)
    if id == 0:
        py.draw.rect(screen, "#798394", properties, border_top_left_radius=20, border_bottom_right_radius=20) 
    elif id == 1:
        py.draw.rect(screen, "red", properties, border_radius=18)
        draw_text('1')
    elif id == 2:
        py.draw.rect(screen, "black", properties, border_radius=18)
        draw_text('2', (255, 255, 255))
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
        py.draw.rect(screen, "light blue", properties, border_radius=18)
        draw_text('6')
    elif id == 7:
        py.draw.rect(screen, "#B5333C", properties, border_radius=18)
        draw_text('7', (255, 255, 255), bold=True)
    elif id == 21:
        py.draw.rect(screen, "#007f00", properties, border_radius=18)
        draw_text('21',(255, 255, 255), bold=True)
    else:
        py.draw.rect(screen, "beige", properties, border_radius=3)
        draw_text(str(id), bold=True)

def draw(loading = False):
    screen.fill("white")
    if loading:
        print(loading)
        positionY = (width+score_width) // 2 - square_side // 2
        positionX = height // 2 - square_side // 2
        text_surface = fontBold.render('Loading...', True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(positionY + square_side // 2, positionX + square_side // 2))
        screen.blit(text_surface, text_rect)
        r1, r2, r3 = random.randint(1234, 4567), random.randint(123, 999), random.randint(4567, 8901)
        r4 = r1-r2+r3
        r5 = f"Fact: {r1} - {r2} + {r3} = {r4}"
        subtext = ["Please wait while the game loads.", "SEVEN!!!", r5, "\"4 \" * 3 = 4 4 4 ", "Do you think Verdana is the best font?", "asdbfasdfajkshdfbkewyboyubiuqwbfub", "Fortunately batteries are included with the computer", "Gravity is installed in this game, use at your own risk", "Hello!", "Hexafluorosilicic acid is my favorite molecule", "Definitely not a game by Gavin"][random.randint(0, 10)]
        subtext_surface = font.render(subtext, True, (100, 100, 100))
        subtext_rect = subtext_surface.get_rect(center=(positionY + square_side // 2, positionX + square_side // 2 + 40))
        screen.blit(subtext_surface, subtext_rect)
        return
    diff = gap-square_side
    
    # (squares' sizes + space in between)
 
    cx = (width - grid_width)//2
    cy = (height - grid_height)//2
        #draw square underlay
    py.draw.rect(screen, "#96a0b0", (cx-10, cy-10, grid_width+20, grid_height+20), border_radius=18)
        #draw sizexsize grid of squares
    for rows in range(size):
            for cols in range(size):
                draw_rect(game_state[rows][cols], cols, rows)
def draw_left_side():
    # Draw a moves counter at the top left corner
    moves_text = str(moves)
    moves_font = py.font.SysFont("Verdana", 96, bold=True)
    moves_surface = moves_font.render(moves_text, True, (0, 0, 0))
    screen.blit(moves_surface, (width, 20))

    # Add a smaller 'moves left' text under the number
    moves_left_font = py.font.SysFont("Verdana", 32, bold=False)
    moves_left_surface = moves_left_font.render("moves left" if moves != 1 else "move left!!", True, (0, 0, 0))
    moves_left_rect = moves_left_surface.get_rect()
    # Place it centered under the big number
    moves_left_x = width
    moves_left_y = 20 + moves_surface.get_height() + 10
    screen.blit(moves_left_surface, (moves_left_x, moves_left_y))
    # Allocate space for some body text in the remaining space (below moves counter)
    # Load and display the instructions image below the moves counter
    try:
        instructions_image = py.image.load("instructions.png")
        # Scale the image to fit the available width (score panel)
        max_img_width = score_width - 20
        scale_factor = min(1.0, max_img_width / instructions_image.get_width())
        img_width = int(instructions_image.get_width() * scale_factor)
        img_height = int(instructions_image.get_height() * scale_factor)
        instructions_image = py.transform.smoothscale(instructions_image, (img_width, img_height))
        body_surface = instructions_image
    except Exception as e:
        # If image fails to load, show fallback text
        fallback_font = py.font.SysFont("Verdana", 20)
        body_surface = fallback_font.render("Instructions image not found.", True, (200, 0, 0))
    # Place it below the 'moves left' text, with some padding
    body_x = moves_left_x
    body_y = moves_left_y + moves_left_rect.height
    screen.blit(body_surface, (body_x, body_y))
    py.display.flip()
def score_screen():
    print('hi')
    global score
    score = sum(sum(row) for row in game_state) * 7
    # Show a simple score screen
    screen.fill("gray")
    # Draw the score in the center of the main play area
    score_font = py.font.SysFont("Verdana", 72, bold=True)
    score_text = f"Score: {score}"
    score_surface = score_font.render(score_text, True, (0, 0, 0))
    score_rect = score_surface.get_rect(center=((width+score_width) // 2, height // 2 - 40))
    screen.blit(score_surface, score_rect)

    # Draw a "Game Over" or "Moves Over" message
    over_font = py.font.SysFont("Verdana", 48, italic=True)
    over_surface = over_font.render("NO moves left!", True, (200, 0, 0))
    over_rect = over_surface.get_rect(center=((width+score_width) // 2, height // 2 + 40))
    screen.blit(over_surface, over_rect)

    # Optionally, draw instructions to quit or restart
    info_font = py.font.SysFont("Verdana", 28)
    info_surface = info_font.render("Press ESC to quit", True, (100, 100, 100))
    info_rect = info_surface.get_rect(center=((width+score_width) // 2, height // 2 + 100))
    screen.blit(info_surface, info_rect)

    py.display.flip()
    # Wait for ESC or window close
    waiting = True
    while waiting:
        for event in py.event.get():
            if event.type == py.QUIT:
                py.quit()
                exit()
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    py.quit()
                    exit()
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
        GS.check_and_merge(game_state, size)
        if has_state_changed():
            state_changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        draw()
        if state_speed == 3: py.display.flip()
        clock.tick(state_speed)
        
        GS.gravity(game_state, size)
        if has_state_changed():
            state_changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        draw()
        if state_speed == 3: py.display.flip()
        clock.tick(state_speed)

        GS.fill_game_state(game_state, size)
        if has_state_changed():
            state_changed = True
            last_state = [[game_state[row][col] for col in range(size)] for row in range(size)]
        
        
        draw()
        if state_speed == 3: py.display.flip()
        clock.tick(state_speed)
    state_speed = 3

draw(loading=True)
py.display.flip()

while running:   
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

        if event.type == py.KEYDOWN:
            row = 0 if (row==None) else row
            col = 0 if (col==None) else col
            if event.key == py.K_w:
                row = (row - 1) % size
            elif event.key == py.K_s:
                row = (row + 1) % size
            elif event.key == py.K_a:
                col = (col - 1) % size
            elif event.key == py.K_d:
                col = (col + 1) % size
            elif event.key == py.K_SPACE:
                if locked_cursor_pos == None: locked_cursor_pos = [row, col]
                else: 
                    moves -= 1
                    r1, c1 = locked_cursor_pos
                    r2, c2 = cursor_pos
                    game_state[r1][c1], game_state[r2][c2] = game_state[r2][c2], game_state[r1][c1]
                    locked_cursor_pos = None
                    state_changed = True
            cursor_pos = [row, col]
    
    
    chain_loop()
    draw()
    
    if cursor_pos:
        highlight_color = (0, 0, 255)  # bright green
        highlight_thickness = 5
        highlight_rect = (
            cursor_pos[1] * gap + (width - grid_width)//2,
            cursor_pos[0] * gap + (height - grid_height)//2,
            square_side, square_side
        )
        py.draw.rect(screen, highlight_color, highlight_rect, highlight_thickness, border_radius=18)
    if locked_cursor_pos:
        highlight_color = (255, 120, 225)  # orange
        highlight_thickness = 8
        highlight_rect = (
            locked_cursor_pos[1] * gap + (width - grid_width)//2,
            locked_cursor_pos[0] * gap + (height - grid_height)//2,
            square_side, square_side
        )
        py.draw.rect(screen, highlight_color, highlight_rect, highlight_thickness, border_radius=18)
    draw_left_side()
    if moves == 0:
        score_screen()
    py.display.flip()
    clock.tick(31)

py.quit()
print("done")