class memGrid:
    def __init__(self, grid: list[int], possible_grids: list[list], grids_chosen: list[int], parent_memGrid) -> None:
        self.grid = grid
        self.possible_grids = possible_grids
        self.grids_chosen = grids_chosen
        self.parent_memGrid = parent_memGrid
        self.children = []

GRID = [0, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0,
        0, 5, 2, 0, 0, 0,
        0, 0, 3, 7, 0, 0,
        0, 1, 2, 3, 7, 0,
        0, 0, 4, 0, 0, 0]
MAX_MOVES = 11

INTERACTALBE = [3, 4, 5, 6, 7, 8]
COL6 = [5, 11, 17, 23, 29, 35]

original_grid: memGrid

def move_up(grid: list[int], index: int) -> list[int]:
    local_grid = grid.copy()

    if index > 5:
        if local_grid[index - 6] == 0:
            local_grid[index - 6] = local_grid[index]
            local_grid[index] = 0
        elif local_grid[index - 6] == 1:
            local_grid[index] = 0
        else:
            if local_grid[index - 12] == 0:
                local_grid[index - 12] = local_grid[index - 6]
                local_grid[index - 6] = local_grid[index]
                local_grid[index] = 0
            elif local_grid[index - 12] == 1:
                local_grid[index - 6] = local_grid[index]
                local_grid[index] = 0
            else:
                if local_grid[index - 18] == 0:
                    local_grid[index - 18] = local_grid[index - 12]
                    local_grid[index - 12] = local_grid[index - 6]
                    local_grid[index - 6] = local_grid[index]
                    local_grid[index] = 0
                elif local_grid[index - 18] == 1:
                    local_grid[index - 12] = local_grid[index - 6]
                    local_grid[index - 6] = local_grid[index]
                    local_grid[index] = 0
                else:
                    if local_grid[index - 24] == 0:
                        local_grid[index - 24] = local_grid[index - 18]
                        local_grid[index - 18] = local_grid[index - 12]
                        local_grid[index - 12] = local_grid[index - 6]
                        local_grid[index - 6] = local_grid[index]
                        local_grid[index] = 0
                    elif local_grid[index - 24] == 1:
                        local_grid[index - 18] = local_grid[index - 12]
                        local_grid[index - 12] = local_grid[index - 6]
                        local_grid[index - 6] = local_grid[index]
                        local_grid[index] = 0
                    else:
                        if local_grid[index - 30] == 0:
                            local_grid[index - 30] = local_grid[index - 24]
                            local_grid[index - 24] = local_grid[index - 18]
                            local_grid[index - 18] = local_grid[index - 12]
                            local_grid[index - 12] = local_grid[index - 6]
                            local_grid[index - 6] = local_grid[index]
                            local_grid[index] = 0
                        elif local_grid[index - 30] == 1:
                            local_grid[index - 24] = local_grid[index - 18]
                            local_grid[index - 18] = local_grid[index - 12]
                            local_grid[index - 12] = local_grid[index - 6]
                            local_grid[index - 6] = local_grid[index]
                            local_grid[index] = 0


    return local_grid

def move_right(grid: list[int], index: int) -> list[int]:
    local_grid = grid.copy()

    if index not in COL6:
        if local_grid[index + 1] == 0:
            local_grid[index + 1] = local_grid[index]
            local_grid[index] = 0
        elif local_grid[index + 1] == 1:
            local_grid[index] = 0
        else:
            if local_grid[index + 2] == 0:
                local_grid[index + 2] = local_grid[index + 1]
                local_grid[index + 1] = local_grid[index]
                local_grid[index] = 0
            elif local_grid[index + 2] == 1:
                local_grid[index + 1] = local_grid[index]
                local_grid[index] = 0
            elif index + 2 not in COL6:
                if local_grid[index + 3] == 0:
                    local_grid[index + 3] = local_grid[index + 2]
                    local_grid[index + 2] = local_grid[index + 1]
                    local_grid[index + 1] = local_grid[index]
                    local_grid[index] = 0
                elif local_grid[index + 3] == 1:
                    local_grid[index + 2] = local_grid[index + 1]
                    local_grid[index + 1] = local_grid[index]
                    local_grid[index] = 0
                elif index + 3 not in COL6:
                    if local_grid[index + 4] == 0:
                        local_grid[index + 4] = local_grid[index + 3]
                        local_grid[index + 3] = local_grid[index + 2]
                        local_grid[index + 2] = local_grid[index + 1]
                        local_grid[index + 1] = local_grid[index]
                        local_grid[index] = 0
                    elif local_grid[index + 4] == 1:
                        local_grid[index + 3] = local_grid[index + 2]
                        local_grid[index + 2] = local_grid[index + 1]
                        local_grid[index + 1] = local_grid[index]
                        local_grid[index] = 0
                    elif index + 4 not in COL6:
                        if local_grid[index + 5] == 0:
                            local_grid[index + 5] = local_grid[index + 4]
                            local_grid[index + 4] = local_grid[index + 3]
                            local_grid[index + 3] = local_grid[index + 2]
                            local_grid[index + 2] = local_grid[index + 1]
                            local_grid[index + 1] = local_grid[index]
                            local_grid[index] = 0
                        elif local_grid[index + 5] == 1:
                            local_grid[index + 4] = local_grid[index + 3]
                            local_grid[index + 3] = local_grid[index + 2]
                            local_grid[index + 2] = local_grid[index + 1]
                            local_grid[index + 1] = local_grid[index]
                            local_grid[index] = 0

        

    return local_grid

def move_down(grid: list[int], index: int) -> list[int]:
    local_grid = grid.copy()

    if index < 30:
        if local_grid[index + 6] == 0:
            local_grid[index + 6] = local_grid[index]
            local_grid[index] = 0
        elif local_grid[index + 6] == 1:
            local_grid[index] = 0
        else:
            if local_grid[index + 12] == 0:
                local_grid[index + 12] = local_grid[index + 6]
                local_grid[index + 6] = local_grid[index]
                local_grid[index] = 0
            elif local_grid[index + 12] == 1:
                local_grid[index + 6] = local_grid[index]
                local_grid[index] = 0
            else:
                if local_grid[index + 18] == 0:
                    local_grid[index + 18] = local_grid[index + 12]
                    local_grid[index + 12] = local_grid[index + 6]
                    local_grid[index + 6] = local_grid[index]
                    local_grid[index] = 0
                elif local_grid[index + 18] == 1:
                    local_grid[index + 12] = local_grid[index + 6]
                    local_grid[index + 6] = local_grid[index]
                    local_grid[index] = 0
                else:
                    if local_grid[index + 24] == 0:
                        local_grid[index + 24] = local_grid[index + 18]
                        local_grid[index + 18] = local_grid[index + 12]
                        local_grid[index + 12] = local_grid[index + 6]
                        local_grid[index + 6] = local_grid[index]
                        local_grid[index] = 0
                    elif local_grid[index + 24] == 1:
                        local_grid[index + 18] = local_grid[index + 12]
                        local_grid[index + 12] = local_grid[index + 6]
                        local_grid[index + 6] = local_grid[index]
                        local_grid[index] = 0
                    else:
                        if local_grid[index + 30] == 0:
                            local_grid[index + 30] = local_grid[index + 24]
                            local_grid[index + 24] = local_grid[index + 18]
                            local_grid[index + 18] = local_grid[index + 12]
                            local_grid[index + 12] = local_grid[index + 6]
                            local_grid[index + 6] = local_grid[index]
                            local_grid[index] = 0
                        elif local_grid[index + 30] == 1:
                            local_grid[index + 24] = local_grid[index + 18]
                            local_grid[index + 18] = local_grid[index + 12]
                            local_grid[index + 12] = local_grid[index + 6]
                            local_grid[index + 6] = local_grid[index]
                            local_grid[index] = 0


    return local_grid

def move_left(grid: list[int], index: int) -> list[int]:
    local_grid = grid.copy()

    if (index / 6) % 1 != 0:
        if local_grid[index - 1] == 0:
            local_grid[index - 1] = local_grid[index]
            local_grid[index] = 0
        elif local_grid[index - 1] == 1:
            local_grid[index] = 0
        else:
            if local_grid[index - 2] == 0:
                local_grid[index - 2] = local_grid[index - 1]
                local_grid[index - 1] = local_grid[index]
                local_grid[index] = 0
            elif local_grid[index - 2] == 1:
                local_grid[index - 1] = local_grid[index]
                local_grid[index] = 0
            else:
                if local_grid[index - 3] == 0:
                    local_grid[index - 3] = local_grid[index - 2]
                    local_grid[index - 2] = local_grid[index - 1]
                    local_grid[index - 1] = local_grid[index]
                    local_grid[index] = 0
                elif local_grid[index - 3] == 1:
                    local_grid[index - 2] = local_grid[index - 1]
                    local_grid[index - 1] = local_grid[index]
                    local_grid[index] = 0
                else:
                    if local_grid[index - 4] == 0:
                        local_grid[index - 4] = local_grid[index - 3]
                        local_grid[index - 3] = local_grid[index - 2]
                        local_grid[index - 2] = local_grid[index - 1]
                        local_grid[index - 1] = local_grid[index]
                        local_grid[index] = 0
                    elif local_grid[index - 4] == 1:
                        local_grid[index - 3] = local_grid[index - 2]
                        local_grid[index - 2] = local_grid[index - 1]
                        local_grid[index - 1] = local_grid[index]
                        local_grid[index] = 0
                    else:
                        if local_grid[index - 5] == 0:
                            local_grid[index - 5] = local_grid[index - 4]
                            local_grid[index - 4] = local_grid[index - 3]
                            local_grid[index - 3] = local_grid[index - 2]
                            local_grid[index - 2] = local_grid[index - 1]
                            local_grid[index - 1] = local_grid[index]
                            local_grid[index] = 0
                        elif local_grid[index - 5] == 1:
                            local_grid[index - 4] = local_grid[index - 3]
                            local_grid[index - 3] = local_grid[index - 2]
                            local_grid[index - 2] = local_grid[index - 1]
                            local_grid[index - 1] = local_grid[index]
                            local_grid[index] = 0


    return local_grid

def solve(grid: list[int]):
    solved = False
    local_grid = grid.copy()

    original_grid = memGrid(local_grid.copy(), [], [], None)
    current_grid = original_grid
    moves_played = 0

    while (not solved):
        step_grids: list[list] = []
        step_grids_scores: list[int] = []

        num_index = 0
        for num in local_grid:
            if num in INTERACTALBE:
                match num:
                    case 3:
                        local_step_grid = local_grid.copy()
                        local_step_grid[num_index] = 0
                        step_grids.append(local_step_grid)
                    case 4:
                        step_grids.append(move_up(local_grid, num_index))
                    case 5:
                        step_grids.append(move_right(local_grid, num_index))
                    case 6:
                        step_grids.append(move_down(local_grid, num_index))
                    case 7:
                        step_grids.append(move_left(local_grid, num_index))
                    case 8:
                        local_step_grid = local_grid.copy()
                        local_step_grid[num_index] = 1
                        step_grids.append(local_step_grid)
            num_index += 1
                        
        for step_grid in step_grids:
            score = 100
            for n in step_grid:
                if n is not 0 and n is not 1:
                    score -= 10
            
            step_grids_scores.append(score)

        index = 0
        for grid in step_grids:
            print("GRIDS")
            print(str(step_grids_scores[index]))
            print("------")
            for y in range(6):
                print(str(grid[0 + (y * 6)]) + ", " + str(grid[1 + (y * 6)]) + ", " + str(grid[2 + (y * 6)]) + ", " + str(grid[3 + (y * 6)]) + ", " + str(grid[4 + (y * 6)]) + ", " + str(grid[5 + (y * 6)]) + ",")
            print("------")

            index += 1

        paired_list = zip(step_grids_scores, step_grids)
        sorted_paired_list = sorted(paired_list, reverse=True)
        if sorted_paired_list:
            sorted_step_grids_scores, sorted_step_grids = zip(*sorted_paired_list)
        step_grids = list(sorted_step_grids)
        step_grids_scores = list(sorted_step_grids_scores)

        step_grids_scores.sort(reverse=True)
        

        print("CHOSEN GRID")
        print(str(step_grids_scores[0]))
        print("------")
        for y in range(6):
            print(str(step_grids[0][0 + (y * 6)]) + ", " + str(step_grids[0][1 + (y * 6)]) + ", " + str(step_grids[0][2 + (y * 6)]) + ", " + str(step_grids[0][3 + (y * 6)]) + ", " + str(step_grids[0][4 + (y * 6)]) + ", " + str(step_grids[0][5 + (y * 6)]) + ",")
        print("------")
        
        print("NEW STEP")

        if step_grids_scores[0] >= 100:
            solved = True

        if not solved:
            if moves_played <= MAX_MOVES:
                if current_grid.parent_memGrid and current_grid.parent_memGrid.grid == current_grid.grid or current_grid.grids_chosen.count == current_grid.possible_grids.count:
                    current_grid = current_grid.parent_memGrid
                    local_grid = current_grid.grid.copy()
                    moves_played -= 1
                else:
                    current_grid.possible_grids = step_grids.copy()
                    chosen_grid = 0
                    if len(current_grid.grids_chosen) > 1:
                        has_chose_grid = False

                        while (has_chose_grid == False):
                            chosen_grid += 1
                            if chosen_grid not in current_grid.grids_chosen:
                                has_chose_grid = True
                            if chosen_grid >= len(current_grid.possible_grids) and current_grid.parent_memGrid:
                                has_chose_grid = True
                                current_grid = current_grid.parent_memGrid
                                local_grid = current_grid.grid.copy()
                                chosen_grid = -1
                                moves_played -= 1
                            elif not current_grid.parent_memGrid:
                                print("Failed to finish")
                                break

                    if chosen_grid is not -1:
                        current_grid.grids_chosen.append(chosen_grid)

                        new_grid = memGrid(step_grids[chosen_grid].copy(), [], [], current_grid)
                        current_grid.children.append(new_grid)
                        current_grid = new_grid

                        local_grid = step_grids[chosen_grid].copy()
                        moves_played += 1
            else:
                current_grid = current_grid.parent_memGrid
                local_grid = current_grid.grid.copy()
                chosen_grid = -1
                moves_played -= 1

    

solve(GRID)