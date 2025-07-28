import json

CLICKABLE = [3, 4, 5, 6, 7, 8]

with open('entities.json', "r") as f:
    entities = json.load(f)
levels = entities["game"]["levels"]["sequence"]

def loop(grid):
    local_grid = grid
    score = 100

    for num in entities[level]["puzzle"]["grid"]:
        if num in CLICKABLE:
            score -= 10

    index = 0
    for num in local_grid:
        if num in CLICKABLE:
            match num:
                case 3:
                    local_grid[index] = 0
                case 4:
                    if index > 5:
                        local_grid[index] = 0
                        local_grid[index - 6] = 4


        
        index += 1
    
    print(local_grid)


for level in levels:
    if entities[level]["puzzle"]["grid"]:
        grid = entities[level]["puzzle"]["grid"]

        print(level)
        print(grid)

        loop(grid)