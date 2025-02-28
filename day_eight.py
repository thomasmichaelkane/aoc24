from lib import *
import time

def run():

    #### SETUP #####

    # read antenna map
    antenna_map = read_lines(get_filename())
    w, h = len(antenna_map[0]), len(antenna_map)
    
    # create separate boolean arrays for each frequency and add to dictionary
    frequency_maps = {}
    for i in range(w):
        for j in range(h):
            if antenna_map[j][i] == ".":
                continue
            else:
                if antenna_map[j][i] not in frequency_maps:
                    frequency_maps[antenna_map[j][i]] = blank_map(w, h)
                frequency_maps[antenna_map[j][i]][j][i] = 1
    
    # also store the separate frequency antenna locations as coordinates
    frequency_coords = {k: map_to_coords(frequency_maps[k]) for k in frequency_maps}
            
    t0 = time.time()

    #### PART ONE & TWO #####
    
    antinode_maps, resonant_maps = {}, {}

    # iterate through every frequency antenna
    for key in frequency_maps:
        
        # blank maps for antinodes (pt1) and resonant antinodes (pt2)
        antinode_maps[key], resonant_maps[key] = blank_map(w, h), blank_map(w, h)
        
        # create all pairwise (r=2) combinations of antenna coordinates
        permutations = list(itertools.combinations(frequency_coords[key], r=2))
        
        for i, permutation in enumerate(permutations):

            (y0, x0), (y1, x1) = permutation
            dx0, dy0 = x0-x1, y0-y1
            
            antinodes = []
            v = 1
            
            # stop adding antinodes when the distance is greater than the largest dimension of the whole map
            while abs(min(v*dx0, v*dy0)) < max(w, h):
                
                # append new 'peak' of the wave
                dx, dy = v*dx0, v*dy0
                antinodes.append((x0+dx, y0+dy))
                antinodes.append((x1-dx, y1-dy))
                v += 1
            
            # add all antinodes (Ax, Ay) which fit on the maps
            for i, (Ax, Ay) in enumerate(antinodes):
                if (Ax >= 0) and (Ay >= 0) and (Ax < w) and (Ay < h): 
                    resonant_maps[key][Ay][Ax] = 1
                    
                    # (first iteration) only add antinodes where v = 1 (special case for pt1)
                    if i <= 1:
                        antinode_maps[key][Ay][Ax] = 1
            
    # union_map is just an element-wise AND operator on arrays, that works with lists and dictionaries
    union_antinodes = union_map(antinode_maps)
    union_resonant_antinodes = union_map([union_map(resonant_maps), union_map(frequency_maps)])

    t1 = time.time()
    t2 = time.time()

    #### ANSWERS #####

    part_one = matrix_sum(union_antinodes)
    part_two = matrix_sum(union_resonant_antinodes)
    log_answers(part_one, part_two, t0, t1, t2)
    
#### FUNCTIONS #####

####

if __name__ == '__main__':
    run()