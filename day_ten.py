from lib import *
import time
from collections import deque

def run():

    #### SETUP #####

    char_map = read_char_map(get_filename(), to_int=True)
    w, h = len(char_map[0]), len(char_map)
    
    trailhead_map = [[not c for c in row] for row in char_map]
    trailhead_coords = {i: (x[1], x[0]) for i, x in enumerate(map_to_coords(trailhead_map))}
    
    t0 = time.time()

    #### PART ONE #####
    
    trailhead_dest, trailhead_dest_map = {}, blank_map(w, h, x=-1)

    for k in trailhead_coords:

        trailhead_dest[k] = bfs_hikes(char_map, trailhead_coords[k])
        trailhead_dest_map[trailhead_coords[k][1]][trailhead_coords[k][0]] = len(trailhead_dest[k])
        
    t1 = time.time()
    
    #### PART TWO #####
    
    trailhead_rating, trailhead_rating_map = {}, blank_map(w, h, x=-1)

    for k in trailhead_coords:

        trailhead_rating[k] = bfs_hikes(char_map, trailhead_coords[k], unique=False)
        trailhead_rating_map[trailhead_coords[k][1]][trailhead_coords[k][0]] = len(trailhead_rating[k])
        
    t2 = time.time()

    #### ANSWERS #####

    part_one = sum([len(trailhead_dest[k]) for k in trailhead_dest])
    part_two = sum([len(trailhead_rating[k]) for k in trailhead_rating])
    log_answers(part_one, part_two, t0, t1, t2)
    
#### FUNCTIONS #####

def bfs_hikes(grid, start, unique=True):

    w, h = len(grid[0]), len(grid)  # Dimensions of the grid               # To keep track of visited nodes
    queue = deque([start])                # Initialize the queue with the start position
    
    hikes = []
    
    # Possible moves: left, right, up, down 
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x0, y0 = queue.popleft()

        for dx, dy in directions:
            x, y = x0 + dx, y0 + dy

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