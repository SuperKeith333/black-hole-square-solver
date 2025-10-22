import time

class memory_grid:
    def __init__(self):
        self.possible_grids = {}
        self.grid = ()
        self.parent_memory_grid = None
        self.played = False

GRID = [0, 0, 0, 0, 0, 0,
        0, 0, 1, 0, 0, 0,
        0, 5, 2, 0, 0, 0,
        0, 0, 3, 7, 0, 0,
        0, 1, 2, 3, 7, 0,
        0, 0, 4, 0, 0, 0]
MAX_MOVES = 11

INTERACTALBE = [3, 4, 5, 6, 7, 8]
COL0 = [0, 6, 12, 18, 24, 30]
COL6 = [5, 11, 17, 23, 29, 35]

def move_up(grid, index) -> tuple:
    possible_grid = list(grid)

    if index > 5:
        index_to_check = 0
        finished = False
        while not finished:
            if possible_grid[(index - 6) - (6 * index_to_check)] != 0 and possible_grid[(index - 6) - (6 * index_to_check)] != 1:
                index_to_check += 1
            else:
                if possible_grid[(index - 6) - (6 * index_to_check)] == 0:
                    for j in reversed(range(index_to_check + 1)):
                        possible_grid[(index - 6) - (6 * j)] = possible_grid[index - (6 * (j))]
                        possible_grid[index - (6 * j)] = 0
                    finished = True
                elif possible_grid[(index - 6) - (6 * index_to_check)] == 1:
                    for j in reversed(range(index_to_check)):
                        if possible_grid[(index - 6) - (6 * j)] != 1:
                            possible_grid[(index - 6) - (6 * j)] = possible_grid[index - (6 * (j))]
                        possible_grid[index - (6 * j)] = 0

                    if index_to_check <= 0:
                        possible_grid[index] = 0

                    finished = True

    return tuple(possible_grid)
def move_down(grid, index) -> tuple:
    possible_grid = list(grid)

    if index < 30:
        index_to_check = 0
        finished = False
        while not finished:
            if (index + 6) + (6 * index_to_check) <= 35 and possible_grid[(index + 6) + (6 * index_to_check)] != 0 and possible_grid[(index + 6) + (6 * index_to_check)] != 1:
                index_to_check += 1
            elif (index + 6) + (6 * index_to_check) <= 35:
                if possible_grid[(index + 6) + (6 * index_to_check)] == 0:
                    for j in reversed(range(index_to_check + 1)):
                        possible_grid[(index + 6) + (6 * j)] = possible_grid[index + (6 * (j))]
                        possible_grid[index + (6 * j)] = 0
                    finished = True
                elif possible_grid[(index + 6) + (6 * index_to_check)] == 1:
                    for j in reversed(range(index_to_check)):
                        if possible_grid[(index + 6) + (6 * j)] != 1:
                            possible_grid[(index + 6) + (6 * j)] = possible_grid[index + (6 * (j))]
                        possible_grid[index + (6 * j)] = 0

                    if index_to_check <= 0:
                        possible_grid[index] = 0

                    finished = True
            else:
                finished = True

    return tuple(possible_grid)
def move_left(grid, index) -> tuple:
    possible_grid = list(grid)

    if index not in COL0:
        index_to_check = 0
        finished = False
        while not finished:
            if possible_grid[index - 1 - index_to_check] != 0 and possible_grid[index - 1 - index_to_check] != 1:
                index_to_check += 1
            else:
                if possible_grid[index - 1 - index_to_check] == 0:
                    for j in reversed(range(index_to_check + 1)):
                        possible_grid[index - 1 - j] = possible_grid[index - j]
                        possible_grid[index - j] = 0
                    finished = True
                elif possible_grid[index - 1 - index_to_check] == 1:
                    for j in reversed(range(index_to_check)):
                        if possible_grid[index - 1 - j] != 1:
                            possible_grid[index - 1 - j] = possible_grid[index - j]
                        possible_grid[index - j] = 0

                    if index_to_check <= 0:
                        possible_grid[index] = 0

                    finished = True

    return tuple(possible_grid)
def move_right(grid, index) -> tuple:
    possible_grid = list(grid)

    if index not in COL6:
        index_to_check = 0
        finished = False
        while not finished:
            if possible_grid[index + 1 + index_to_check] != 0 and possible_grid[index + 1 + index_to_check] != 1:
                index_to_check += 1
            else:
                if possible_grid[index + 1 + index_to_check] == 0:
                    for j in reversed(range(index_to_check + 1)):
                        possible_grid[index + 1 + j] = possible_grid[index + j]
                        possible_grid[index + j] = 0
                    finished = True
                elif possible_grid[index + 1 + index_to_check] == 1:
                    for j in reversed(range(index_to_check)):
                        if possible_grid[index + 1 + j] != 1:
                            possible_grid[index + 1 + j] = possible_grid[index + j]
                        possible_grid[index + j] = 0

                    if index_to_check <= 0:
                        possible_grid[index] = 0

                    finished = True

    return tuple(possible_grid)

def gen_score(grid: tuple) -> int:
    score = 100
    for num in grid:
        if num != 1 and num != 0:
            score -= 10

    return score

def solve(grid: list[int]):
    start_time = time.perf_counter()

    grid_to_solve = tuple(grid)
    solved_grid = False
    moves_played = 0
    root_grid = memory_grid()
    current_grid = root_grid
    current_grid.grid = tuple(grid_to_solve)

    while not solved_grid:
        if not current_grid.possible_grids:
            for i in range(len(current_grid.grid)):
                child_memory_grid = memory_grid()
                match current_grid.grid[i]:
                    case 3:
                        temp = list(current_grid.grid)
                        temp[i] = 0
                        child_memory_grid.grid = tuple(temp)
                    case 4:
                        child_memory_grid.grid = move_up(current_grid.grid, i)
                    case 5:
                        child_memory_grid.grid = move_right(current_grid.grid, i)
                    case 6:
                        child_memory_grid.grid = move_down(current_grid.grid, i)
                    case 7:
                        child_memory_grid.grid = move_left(current_grid.grid, i)
                    case 8:
                        temp = list(current_grid.grid)
                        temp[i] = 1
                        child_memory_grid.grid = tuple(temp)
                if current_grid.grid[i] in INTERACTALBE:
                    if gen_score(child_memory_grid.grid) not in current_grid.possible_grids:
                        current_grid.possible_grids[gen_score(child_memory_grid.grid)] = []
                    current_grid.possible_grids[gen_score(child_memory_grid.grid)].append(child_memory_grid)
                    child_memory_grid.parent_memory_grid = current_grid

        current_grid.possible_grids = dict(sorted(current_grid.possible_grids.items()))

        moves_played += 1
        if len(current_grid.possible_grids.keys()) > 0 and list(current_grid.possible_grids.keys())[0] >= 100:
            solved_grid = True
        else:
            # current_grid = list(current_grid.possible_grids.values())[0]
            # current_grid.played = True

            if moves_played < MAX_MOVES:
                selected_grid = False
                
                for child_grids in current_grid.possible_grids.values():
                    for child_grid in child_grids:
                        if not child_grid.played:
                            current_grid = child_grid
                            current_grid.played = True
                            selected_grid = True
                            break
                    
                    if selected_grid:
                        break
                        

                if not selected_grid:
                    moves_played -= 2
                    current_grid = current_grid.parent_memory_grid

            else:
                moves_played -= 2
                current_grid = current_grid.parent_memory_grid
        print("------")
        for y in range(6):
            print(str(current_grid.grid[0 + (y * 6)]) + ", " + str(current_grid.grid[1 + (y * 6)]) + ", " + str(current_grid.grid[2 + (y * 6)]) + ", " + str(current_grid.grid[3 + (y * 6)]) + ", " + str(current_grid.grid[4 + (y * 6)]) + ", " + str(current_grid.grid[5 + (y * 6)]) + ",")
        print(moves_played)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time

    # Print the result
    print(f"Task executed in {elapsed_time:.6f} seconds")
solve(GRID)