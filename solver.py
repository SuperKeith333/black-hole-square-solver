GRID = [0, 0, 0, 0, 0, 0,
        0, 0, 0, 4, 0, 0,
        0, 0, 0, 3, 0, 0,
        0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0,
        0, 0, 0, 0, 0, 0]

INTERACTALBE = [3, 4, 5, 6, 7, 8]
COL6 = [5, 11, 17, 23, 29, 35]

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
        elif local_grid[index + 1] == 0:
            local_grid[index] = 0
        elif index + 1 not in COL6:
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

    while (not solved):
        step_grids: list[list] = []
        step_grids_scores: list[int] = []

        num_index = 0
        for num in GRID:
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
                if n in INTERACTALBE:
                    score -= 10
            
            step_grids_scores.append(score)

        index = 0
        for grid in step_grids:
            print(str(step_grids_scores[index]))
            print("------")
            for y in range(6):
                print(str(grid[0 + (y * 6)]) + ", " + str(grid[1 + (y * 6)]) + ", " + str(grid[2 + (y * 6)]) + ", " + str(grid[3 + (y * 6)]) + ", " + str(grid[4 + (y * 6)]) + ", " + str(grid[5 + (y * 6)]) + ",")
            print("------")

            index += 1

        prev_highest_score = -100000000
        for score in step_grids_scores:
            if score > prev_highest_score:
                prev_highest_score = score

        print(str(step_grids_scores[step_grids_scores.index(prev_highest_score)]))

        solved = True
    

solve(GRID)