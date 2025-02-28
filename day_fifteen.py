from lib import *
import time
from collections import deque

def run():

    #### SETUP #####

    [grid, instructions] = read_sections(get_filename())
    instructions = list("".join(instructions))
    
    rprint(grid)
    # rprint(instructions)
    
    t0 = time.time()

    #### PART ONE #####

    direction_chars = ['^', '>', 'v', '<']
    movement = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    obstacles_map = [[x == "#" for x in row.strip()] for row in grid]
    boxes_map = [[x == "O" for x in row.strip()] for row in grid]
    # rprint(obstacles_map)
    # rprint(boxes_map)
    
    # travelled_map = [[0]*len(obstacles_map[0]) for _ in range(len(obstacles_map))]

    (x, y) = find_start(grid)
    # (dx0, dy0) = movement[d0]
    
    w, h = len(obstacles_map[0]), len(obstacles_map)
    guard_map = blank_map(w, h, False)
    guard_map[y][x] = True

    #### PART ONE #####
    
    # for instr in instructions:
        
    #     # input(instr)

    #     # map_visualiser(obstacles_map, "#", boxes_map, "O", guard_map, "@")
        
    #     direction = direction_chars.index(instr)
    #     (dx, dy) = movement[direction % len(movement)]
    #     i, j = x + dx, y + dy
    #     # rprint(i, j)
        
    #     # obstacle in way - dont change
    #     if obstacles_map[j][i]:
    #         # rprint("obstacle in way")
    #         continue
        
    #     # box in the way
    #     if boxes_map[j][i]:
    #         # rprint("box in the way")
            
    #         # count how many boxes until there is a gap or obstacle
    #         nbox = 0
    #         i2, j2 = i, j
    #         while boxes_map[j2][i2]:
    #             nbox += 1
    #             i2, j2 = i2 + dx, j2 + dy
            
    #         # if there is no gap, treat as obstacle
    #         if obstacles_map[j2][i2]:
    #             continue
            
    #         # if there is a gap, move all boxes
    #         else:   
    #             for k in range(2, nbox+2):
    #                 xb, yb = x + (k*dx), y + (k*dy)
    #                 boxes_map[yb][xb] = True
                
    #             # create gap where first box was
    #             boxes_map[j][i] = False
        
    #             # update guard location
    #             guard_map[y][x] = False
    #             guard_map[j][i] = True

    #             # update new guard coordinate
    #             x, y = i, j
            
    #     # empty square    
    #     else:
    #         # rprint("the way is clear")
            
    #         # update guard location
    #         guard_map[y][x] = False
    #         guard_map[j][i] = True

    #         # update new guard coordinate
    #         x, y = i, j
            
    # box_gps = []
    
    # for i in range(w):
    #     for j in range(h):
    #         if boxes_map[j][i]:
    #             box_gps.append((100*j)+i)
                
    # part_one = sum(box_gps)
    
    t1 = time.time()

    #### PART TWO #####

    wide_grid = widen_map(grid)
    
    rprint(wide_grid)
    
    t2 = time.time()

    #### ANSWERS #####

    # log_answers(part_one, "#", t0, t1, t2)
    
#### FUNCTIONS #####

def find_start(grid):
    
    for j, row in enumerate(grid):
        for i, char in enumerate(row):
            if char == "@":
                return (i, j)


def map_visualiser(map, char, second_map, second_char, third_map, third_char):
    
    for j in range(len(map)):
        vis_row = []
        for i in range(len(map[0])):
            if map[j][i]:
                vis_row.append(char)
            elif second_map[j][i]:
                vis_row.append(second_char)
            elif third_map[j][i]:
                vis_row.append(third_char)
            else:
                vis_row.append(".")
                
        rprint(vis_row)
        
    print("--------------------------------------------------")
    
def widen_map(grid):

    wide_grid = []
    
    replacements = {"#": ["#","#"], "O": ["[","]"], ".": [".","."], "@": ["@","."]}
    
    for row in grid:
        row = list(row)
        wide_row = []
        for x in row:
            wide_row.extend(replacements[x])
        wide_grid.append(wide_row)
        
    return wide_grid
            
def check_y(box_map, x, y, dy):
    
    dx = 0
    i, j = x, y + dy
    
    check = []
    
    if box_map[j][i] == "]":
        
        check.append((i-1, i, j))
        
    elif box_map[j][i] == "[":
        
        check.append((i, i+1, j))

def box_checks(box_map, start):

    # w, h = len(grid[0]), len(grid)  # Dimensions of the grid               # To keep track of visited nodes
    queue = deque([start])                # Initialize the queue with the start position
    
    boxes_to_move = []
    
    # Possible moves: left, right, up, down 
    # directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        (x01, x02, y0) = queue.popleft()

        (x11, x12, y1) = (x01-1, x01, y0+1)
        (x21, x22, y1) = (x02, x02+1, y0+1)

        if 0 <= x < h and 0 <= y < w:   # Check bounds
            
            if grid[y][x] == (grid[y0][x0] + 1):
                queue.append((x, y))
                
                if grid[y][x] == 9:
                    hikes.append((x, y))
                        
    if unique:
        hikes = set(hikes)
    
    return hikes    

####

if __name__ == '__main__':
    run()