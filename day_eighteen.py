from lib import *
import time
from collections import namedtuple, deque

def run():

    #### SETUP #####
    
    Point = namedtuple('Point', ['x', 'y'])

    bytes = [Point(x=int(line.split(",")[0]), y=int(line.split(",")[1])) for line in read_lines(get_filename())]
    
    w = h = 71
    # w = h = 7
    key_points = {"S": Point(0,0), "E": Point(w-1,h-1)}
    end = key_points["E"]
    
    
    t0 = time.time()

    #### PART ONE #####
    
    n = 1024
    # n = 21
    grids = {"#": blank_map(w, h, False)}
    
    for i in range(n):
        byte = bytes[i]
        grids["#"][byte.y][byte.x] = True
        
    # map_visualiser(grids, key_points)
    
    dist_map = bfs_maze(grids, key_points["S"])
    
    part_one = dist_map[end.y][end.x]
    
    # tab_print(dist_map, grids["#"])
    
    t1 = time.time()

    #### PART TWO #####

    total_n = len(bytes)
    
    n = int(total_n/2)
    chunk = int(total_n/4)
    
    exit_steps = {}
    
    while True:
        
        grids = {"#": blank_map(w, h, False)}
    
        for i in range(n):
            byte = bytes[i]
            grids["#"][byte.y][byte.x] = True

        dist_map = bfs_maze(grids, key_points["S"])
        
        if dist_map[end.y][end.x] != None:
            n += chunk
        else:
            n -= chunk
            
        chunk = int(round(chunk/2))    
        
        if chunk == 0:
            break
        
    
        
    for j in range(n, n+3):
        
        grids = {"#": blank_map(w, h, False)}
    
        for i in range(j):
            byte = bytes[i]
            grids["#"][byte.y][byte.x] = True

        dist_map = bfs_maze(grids, key_points["S"])
        grids[110] = [[True if dist_map[j][i] is not None else False for i in range(w)] for j in range(h)]
        
        # map_visualiser(grids)
        
        exit_steps[j] = dist_map[end.y][end.x] 
    
    rprint(exit_steps)
    # rprint(bytes[3030])
            
    blocking_byte = bytes[min([k for k in exit_steps if exit_steps[k] == None])-1]
    part_two = ",".join([str(blocking_byte.x), str(blocking_byte.y)])
            
    t2 = time.time()

    #### ANSWERS #####

    log_answers(part_one, part_two, t0, t1, t2)
    
#### FUNCTIONS #####

def bfs_maze(maze_maps, start):

    any_map = list(maze_maps.values())[0]
    w, h = len(any_map[0]), len(any_map)
    
    dist_map = blank_map(w, h, None)
    dist_map[start.x][start.y] = 0
    (xs, ys) = (start.x, start.y)

    queue = deque([(xs, ys)]) # Initialize the queue with the start position
    # rprint(queue.popleft())
    
    # Possible moves: right, up, left, down
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    while queue:
        x0, y0 = queue.popleft()
        
        for (dx, dy) in directions:
            
            x, y = x0 + dx, y0 + dy
            dist = dist_map[y0][x0] + 1

            if (0 <= x < w) and (0 <= y < h) and (not maze_maps["#"][y][x]):   # Check bounds
                
                if dist_map[y][x] == None:
                    dist_map[y][x] = dist
                    queue.append((x, y))
                    
                elif dist < dist_map[y][x]:
                    dist_map[y][x] = dist

    return dist_map

####

if __name__ == '__main__':
    run()