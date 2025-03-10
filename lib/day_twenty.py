from .utils import *
import time
from collections import namedtuple, deque

def run(as_example=False):
  
    #### SETUP ####
    
    Point = namedtuple('Point', ['x', 'y'])

    grid = read_char_map(get_filename("20", as_example))
    maze_grids = {"#": char_bool_map(grid, "#")}  
    (xe, ye), (xs, ys) = find_char(grid, "E"), find_char(grid, "S")
    key_squares = {"S": Point(xs, ys), "E": Point(xe, ye)}  
    
    w, h = len(maze_grids["#"][0]), len(maze_grids["#"])
    
    t0 = time.time()

    #### PART ONE #####
    
    # n = 1024
    # n = 21
    # maze_grids = {"#": blank_map(w, h, False)}
    
    # for i in range(n):
    #     byte = bytes[i]
    #     maze_grids["#"][byte.y][byte.x] = True
        
    # map_visualiser(maze_grids, key_squares)
    
    dist_map = bfs_maze(maze_grids, key_squares["S"])
    
    # tab_print(dist_map, maze_grids["#"])
    
    cheat_map = identify_cheat_squares(maze_grids["#"], dist_map)
    
    tab_print(dist_map, maze_grids["#"], cheat_map)
    
    # sum([True for row in cheat_map for x in row if x >= 100])
    
    part_one = sum([True for row in cheat_map for x in row if x >= 100])
    
    # tab_print(dist_map, maze_grids["#"])
    
    t1 = time.time()

    #### PART TWO #####
            
    t2 = time.time()

    #### ANSWERS #####

    log_answers(part_one, "#", t0, t1, t2)
    
#### FUNCTIONS #####

def bfs_maze(maze_grids, start):

    any_map = list(maze_grids.values())[0]
    w, h = len(any_map[0]), len(any_map)
    
    dist_map = blank_map(w, h, None)
    dist_map[start.y][start.x] = 0
    (xs, ys) = (start.x, start.y)

    queue = deque([(xs, ys)]) # Initialize the queue with the start position
    # rprint(queue.popleft())
    
    # Possible moves: right, up, left, down
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    while queue:
        x0, y0 = queue.popleft()
        
        # rprint(x0, y0)
        
        for (dx, dy) in directions:
            
            x, y = x0 + dx, y0 + dy
            dist = dist_map[y0][x0] + 1

            if (0 <= x < w) and (0 <= y < h) and (not maze_grids["#"][y][x]):   # Check bounds
                
                if dist_map[y][x] == None:
                    dist_map[y][x] = dist
                    queue.append((x, y))
                    
                elif dist < dist_map[y][x]:
                    dist_map[y][x] = dist

    return dist_map

def identify_cheat_squares(obstacles, dist_map):
    
    w, h = len(obstacles[0]), len(obstacles)
    cheat_map = blank_map(w, h, False)
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    
    for j in range(1, h-1):
        for i in range(1, w-1):
            
            if obstacles[j][i]:
                
                neighbors = [obstacles[j+dy][i+dx] for (dx, dy) in directions]
                
                cheat_score = ((not neighbors[0] and not neighbors[2]), (not neighbors[1] and not neighbors[3]))
                
                match cheat_score:
                    case (False, False):
                        continue
                    case (True, False):
                        diff = abs(dist_map[j][i-1] - dist_map[j][i+1])
                    case (False, True):
                        diff = abs(dist_map[j-1][i] - dist_map[j+1][i])
                    case (True, True):
                        diff = max(abs(dist_map[j][i-1] - dist_map[j][i+1]),
                                              abs(dist_map[j-1][i] - dist_map[j+1][i]))
                        
                cheat_map[j][i] = diff - 2

                    
    return cheat_map
                    
                    
                    
                    
                    
                
                
    

####

if __name__ == '__main__':
    run()