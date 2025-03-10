from .utils import *
import time
from rich.progress import track

def run(as_example=False):
  
    #### SETUP ####

    char_map = read_char_map(get_filename("12", as_example), pad_char = "#")
    
    w, h = len(char_map[0]), len(char_map)
    
    all_plants = set([x for row in char_map for x in row])
    all_plants.remove("#")
    
    plant_maps = {plant: [[True if x == plant else False for x in row] for row in char_map] for plant in all_plants}
    region_maps, neighbor_maps, areas = {}, {}, {}
    
    for k in plant_maps:
        separate_regions = find_regions_as_local_arrays(plant_maps[k])
        
        for i, region in enumerate(separate_regions):
            region_maps[(k+"-"+str(i))] = region

    t0 = time.time()

    #### PART ONE #####

    for k in track(region_maps):
    
        areas[k] = len([x for row in region_maps[k] for x in row if x])
        
        w, h = len(region_maps[k][0]), len(region_maps[k])
        
        neighbor_maps[k] = blank_map(w, h, 0)
        
        for i in range(1, w-1):
            for j in range(1, h-1):
                
                if region_maps[k][j][i] is True:
                
                    num_neighbors = 0
                    
                    for (x, y) in get_plus_coords(i, j):
                        
                        if region_maps[k][y][x] is False:
                            num_neighbors += 1
                            
                    neighbor_maps[k][j][i] = num_neighbors
        
                   
        neighbor_totals = [(k, matrix_sum(neighbor_maps[k]), areas[k]) for k in neighbor_maps]

    rprint(region_maps['I-1']) 
        
    t1 = time.time()

    #### PART TWO #####
    
    sides = {k: traverse_boundary(region_maps[k]) for k in region_maps}
    sides_single = traverse_boundary(region_maps['I-1'], printing=True)
    
    sides_totals = [(k, sides[k], areas[k]) for k in sides]
    
    rprint(sides_totals)
    
    t2 = time.time()

    #### ANSWERS #####

    part_one = sum([total[1]*total[2] for total in neighbor_totals])
    part_two = sum([total[1]*total[2] for total in sides_totals])
    # part_two = "#"
    log_answers(part_one, part_two, t0, t1, t2)
    
#### FUNCTIONS #####

def traverse_boundary(region, printing=False):
    
    rprint(region)
    
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    for x, v in enumerate(region[1]):
        if v: break
        
    y = 0
    
    nd = 0
    (dx, dy) = d[nd]
    sides = 0
    (i, j) = (x+dx, y+dy)
    k = 0
    
    while (i, j) != (x, 0):
        kd = (nd + 1) % 4
        if region[j+d[kd][1]][i+d[kd][0]] == False:
            # turn right
            nd += 1
            sides += 1
        elif region[j+d[nd][1]][i+d[nd][0]] == False:
            # continue straight
            pass
        elif region[j+d[nd-1][1]][i+d[nd-1][0]] == False:
            # turn left
            nd -= 1
            sides += 1
        else:
            # turn around
            nd -= 2
            sides += 2
        
        nd = nd % 4
        # print(nd)
        (dx, dy) = d[nd]
        # print(dx, dy)
        (i, j) = (i+dx, j+dy)
        
        if printing:
            rprint((i, j), nd, sides)
        # print(i, j)
                
    return sides

def get_plus_coords(x, y):
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    plus_coords = [(x+dx, y+dy) for (dx, dy) in directions]
    
    return plus_coords

####

if __name__ == '__main__':
    run()