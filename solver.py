GRID = [0, 0, 0, 0, 0, 0,
        0, 0, 0, 2, 0, 0,
        0, 0, 0, 2, 0, 0,
        0, 0, 0, 2, 0, 0,
        0, 0, 0, 2, 0, 0,
        0, 0, 0, 4, 0, 0]

INTERACTALBE = [3, 4, 5, 6, 7, 8]

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

def solve(grid: list[int]):
    solved = False
    local_grid = grid.copy()

    while (not solved):
        step_grids: list[list] = []

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
            num_index += 1
                        
        for grid in step_grids:
            print("------")
            for y in range(6):
                print(str(grid[0 + (y * 6)]) + ", " + str(grid[1 + (y * 6)]) + ", " + str(grid[2 + (y * 6)]) + ", " + str(grid[3 + (y * 6)]) + ", " + str(grid[4 + (y * 6)]) + ", " + str(grid[5 + (y * 6)]) + ",")
            print("------")




        solved = True
    

solve(GRID)