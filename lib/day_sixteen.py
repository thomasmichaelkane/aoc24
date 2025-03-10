from .utils import *
import time
from collections import deque

def run(as_example=False):
  
    #### SETUP ####

    grid = read_char_map(get_filename("16", as_example))
    maze_maps = {"#": char_bool_map(grid, "#")}
    key_squares = {"S": find_char(grid, "S"), "E": find_char(grid, "E")}
    
    (xe, ye), (xs, ys) = key_squares["E"], key_squares["S"]
    
    # map_visualiser(maze_maps, key_squares)
    
    t0 = time.time()

    #### PART ONE #####

    turns_map, dist_map = bfs_maze(maze_maps, (xs, ys, 0), (xe, ye))

    w, h = len(turns_map[0]), len(turns_map)
    
    score_map = [[(turns_map[j][i]*1000) + dist_map[j][i]
                    if turns_map[j][i] is not None 
                    else None 
                        for i in range(w)] 
                        for j in range(h)]
    
    tab_print(score_map, maze_maps["#"])

    part_one = score_map[ye][xe]
    
    t1 = time.time()

    #### PART TWO #####

    bp_map = bfs_best_paths(score_map, (xe, ye))

    part_two = matrix_sum(bp_map)
    
    t2 = time.time()

    #### ANSWERS #####

    log_answers(part_one, part_two, t0, t1, t2)
    
#### FUNCTIONS #####

def bfs_maze(maze_maps, start, end):

    any_map = list(maze_maps.values())[0]
    w, h = len(any_map[0]), len(any_map)
    (xs, ys, ds) = start
    
    turns_map, dist_map = blank_map(w, h, None), blank_map(w, h, None)
    turns_map[ys][xs], dist_map[ys][xs] = ds, 0

    queue = deque([start]) # Initialize the queue with the start position
    
    # Possible moves: right, up, left, down
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    while queue:
        x0, y0, d0 = queue.popleft()
        
        wall_ahead = check_for_wall_ahead(maze_maps, x0, y0, d0, directions)

        for i, (dx, dy) in enumerate(directions):
            new_turns = abs(d0 - i)
            if new_turns == 2: continue
            new_turns %= 2
            
            x, y = x0 + dx, y0 + dy
            turns = turns_map[y0][x0] + new_turns
            dist = dist_map[y0][x0] + 1

            if not maze_maps["#"][y][x]:   # Check bounds
                
                if turns_map[y][x] == None:
                    turns_map[y][x] = turns
                    dist_map[y][x] = dist
                    queue.append((x, y, i))
                    
                elif turns < turns_map[y][x]:
                    turns_map[y][x] = turns
                    dist_map[y][x] = dist
                    
                    to_remove = []
                    for (xq, yq, j) in queue:
                        if (xq, yq) == (x, y):
                            to_remove.append((xq, yq, j))
                            
                    [queue.remove(entry) for entry in to_remove] 
                    
                    queue.append((x, y, i))
    
        if wall_ahead and (x0, y0) != end:
            turns_map[y0][x0] += 1

    return turns_map, dist_map

def bfs_best_paths(score_map, start):
    
    w, h = len(score_map[0]), len(score_map)
    (xs, ys) = start
    
    bp_map = blank_map(w, h, False)
    bp_map[ys][xs] = True

    queue = deque([start])                # Initialize the queue with the start position
    
    # Possible moves: right, up, left, down
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    
    while queue:
        
        (x0, y0) = queue.popleft()

        for i, (dx, dy) in enumerate(directions):
            
            x, y = x0 + dx, y0 + dy

            if score_map[y][x] is not None:   # Check bounds
                
                if score_map[y][x] < score_map[y0][x0]:
                    bp_map[y][x] = True
                    queue.append((x, y))
    
    return bp_map
    
def check_for_wall_ahead(maze_maps, x0, y0, d0, directions):
    (dxs, dys), (dxl, dyl), (dxr, dyr) = directions[d0], directions[d0-1], directions[(d0+1)%4]
    if (maze_maps["#"][y0 + dys][x0 + dxs] 
        and not (maze_maps["#"][y0 + dyl][x0 + dxl]
        and maze_maps["#"][y0 + dyr][x0 + dxr])):
            return True 
    else:
            return False

####

if __name__ == '__main__':
    run()