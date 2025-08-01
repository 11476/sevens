
def check_and_merge(game_state, size):
    merges = []
    used = set()  # To prevent a cell from being in more than one merge
    
    # First pass: find all possible merge groups
    all_possible_merges = []
    
    for row in range(size):
        for col in range(size):
            cell = game_state[row][col]
            if cell < 1:
                continue
                
            # Triple merge (cell >= 7)
            if cell >= 7:
                # Horizontal
                if col + 2 < size:
                    if game_state[row][col+1] == cell and game_state[row][col+2] == cell:
                        all_possible_merges.append(([(row, col), (row, col+1), (row, col+2)], cell * 3, 'triple'))
                # Vertical
                if row + 2 < size:
                    if game_state[row+1][col] == cell and game_state[row+2][col] == cell:
                        all_possible_merges.append(([(row, col), (row+1, col), (row+2, col)], cell * 3, 'triple'))
            
            # Sum-to-7 horizontal
            sum_ = cell
            group = [(row, col)]
            for c in range(col+1, size):
                neighbor = game_state[row][c]
                if not (neighbor != 0 and neighbor != 7):
                    break
                sum_ += neighbor
                group.append((row, c))
                if sum_ > 7:
                    break
                if sum_ == 7 and len(group) > 1:
                    all_possible_merges.append((group[:], 7, 'sum7'))
                    break
            
            # Sum-to-7 vertical
            sum_ = cell
            group = [(row, col)]
            for r in range(row+1, size):
                neighbor = game_state[r][col]
                if not (neighbor != 0 and neighbor != 7):
                    break
                sum_ += neighbor
                group.append((r, col))
                if sum_ > 7:
                    break
                if sum_ == 7 and len(group) > 1:
                    all_possible_merges.append((group[:], 7, 'sum7'))
                    break
    
    # Sort merges by priority: triple merges first, then by length (longer first), then by position
    def merge_priority(merge):
        group, value, merge_type = merge
        # Triple merges have highest priority
        if merge_type == 'triple':
            return (0, -len(group), group[0][0], group[0][1])
        # For sum7 merges, longer groups have priority
        return (1, -len(group), group[0][0], group[0][1])
    
    all_possible_merges.sort(key=merge_priority)
    
    # Second pass: apply merges in priority order, avoiding conflicts
    for group, new_value, merge_type in all_possible_merges:
        # Check if any cell in this group is already used
        if any((r, c) in used for r, c in group):
            continue
        
        # Apply this merge
        merges.append((group, new_value))
        used.update(group)
    
    # Third pass: apply all selected merges
    for group, new_value in merges:
        for r, c in group[:-1]:
            game_state[r][c] = 0
        r, c = group[-1]
        game_state[r][c] = new_value
import random
def fill_game_state(game_state, size):
    for row in range(size):
        for col in range(size):
            if game_state[row][col]==0:
                game_state[row][col] = random.randint(1, 7)
def gravity(game_state, size):
    for col in range(size):
        for row in range(size - 2, -1, -1):  # start from second-to-last row upwards
            if game_state[row][col] != 0:
                current_row = row
                while current_row + 1 < size and game_state[current_row + 1][col] == 0:
                    game_state[current_row + 1][col] = game_state[current_row][col]
                    game_state[current_row][col] = 0
                    current_row += 1
