
def check_and_merge(game_state, size):
    for row in range(size):
        for col in range(size):
            cell = game_state[row][col]
            if (cell < 1): continue
            if (cell >= 7):
                # Check to the right for two identical cells
                if col + 2 < size and game_state[row][col+1] == cell and game_state[row][col+2] == cell:
                    game_state[row][col+1] = 0
                    game_state[row][col+2] = cell * 3
                    game_state[row][col] = 0
                # Check downwards for two identical cells
                if row + 2 < size and game_state[row+1][col] == cell and game_state[row+2][col] == cell:
                    game_state[row+1][col] = 0
                    game_state[row+2][col] = cell * 3
                    game_state[row][col] = 0
                continue
            sum = cell
            # to the right
            for c in range(col+1, size):
                neighbor = game_state[row][c]
                if (not (neighbor != 0 and neighbor != 7)): break
                sum += neighbor
                if (sum > 7): break
                if (sum == 7): 
                # set all previously encountered neighbors into 0 and cell to 7
                    for cc in range(col+1, c+1):
                        game_state[row][cc] = 0
                    game_state[row][col] = 7
            sum = cell
            # down (fixed comment)
            for r in range(row+1, size):
                neighbor = game_state[r][col]
                if (not (neighbor != 0 and neighbor != 7)): break
                sum += neighbor
                if (sum > 7): break
                if (sum == 7): 
                    for rr in range(row+1, r+1):
                        game_state[rr][col] = 0
                    game_state[row][col] = 7
import random
def fill_game_state(game_state, size):
    #fill one row
        for col in range(size):
            if game_state[0][col]==0:
                game_state[0][col] = random.randint(7, 7)
def gravity(game_state, size):
    for col in range(size):
        for row in range(size - 2, -1, -1):  # start from second-to-last row upwards
            if game_state[row][col] != 0:
                current_row = row
                while current_row + 1 < size and game_state[current_row + 1][col] == 0:
                    game_state[current_row + 1][col] = game_state[current_row][col]
                    game_state[current_row][col] = 0
                    current_row += 1
