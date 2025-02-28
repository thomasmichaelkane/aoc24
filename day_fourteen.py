from lib import *
import time
from operator import mul
from functools import reduce

def run():

    #### SETUP #####
    
    w, h = 101, 103
    t = 100
    
    grid = blank_map(w, h, 0)

    robots_info = [(line.split()[0].strip("p="), line.split()[1].strip("v=")) for line in read_lines(get_filename())]
    robots = [{"p": (int(info[0].split(",")[0]), int(info[0].split(",")[1])), "v": (int(info[1].split(",")[0]), int(info[1].split(",")[1]))} for info in robots_info]
    
    # rprint(robots)
    
    for robot in robots:
        (i, j) = robot["p"]
        grid[j][i] += 1
    
    # rprint(grid)
    
    t0 = time.time()

    #### PART ONE #####
    
    final_grid = blank_map(w, h, 0)
    
    for robot in robots:
        (dx, dy) = (robot["v"][0]*t, robot["v"][1]*t)
        (x, y) = ((robot["p"][0] + dx) % w, (robot["p"][1] + dy) % h)
        # rprint(x, y)
        final_grid[y][x] += 1
        robot["f"] = (x, y)

    # rprint(final_grid)
    
    qc = quad_coords(w, h)
    
    # rprint(y1, x1)
    quads = [[row[x0:x1] for row in final_grid[y0:y1]] for (y0, y1, x0, x1) in qc]
    
    # rprint(quad)
    
    
    # [row[0:x1] for row in final_grid[0:y1]]
    # quads = (final_grid[0:y1][0:x1], final_grid[0:y1][x2:w], final_grid[y2:h][0:x1], final_grid[y2:h][x2:w])
    
    # for quad in quads:
    #     rprint(quad)
        
    quad_sums = [matrix_sum(quad) for quad in quads]
 
    t1 = time.time()

    #### PART TWO #####
    
    pt2_grid = blank_map(w, h, 0)
    
    for robot in robots:
        x0, y0 = robot["p"]
        pt2_grid[y0][x0] += 1

    # show_arr(pt2_grid)
    
    t = 0
    
    while True:
        
        t += 1
        connectivity_score = 0

        for robot in robots:
            x0, y0 = robot["p"]
            (dx, dy) = (robot["v"][0], robot["v"][1])
            pt2_grid[y0][x0] -= 1
            (x, y) = ((x + dx) % w, (y + dy) % h)
            # rprint(x, y)
            pt2_grid[y][x] += 1
            robot["p"] = (x, y)
            
        neighbor_sums = []
        
        # qc = quad_coords(w, h)
    
        # rprint(y1, x1)
        # quads = [[row[x0:x1] for row in pt2_grid[y0:y1]] for (y0, y1, x0, x1) in qc]
        # quad_sums = [matrix_sum(quad) for quad in quads]
        # rprint(quad_sums)
        
        # if max(quad_sums) - min(quad_sums) < 5:
        show_arr(pt2_grid)
            
        # for robot in robots:
        #     x, y = robot["p"]
            
        #     robot_neighbors = [pt2_grid[(y + dy) % h][(x + dx) % w] for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]]
            
        #     neighbor_sums.append(sum(robot_neighbors))
            
        #     # if sum([pt2_grid[(y + dy) % h][(x + dx) % w] for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]]) > 1:
            #     connectivity_score += 1
        
        # mmax = matrix_max(pt2_grid)
        # rprint(pt2_grid)
        # rprint(sum(neighbor_sums))
        # symscore = symmetry_score(pt2_grid)
            
        # rprint(symscore)
        
        # rprint(connectivity_score)
            
        # if connectivity_score > 15:
            # show_arr(pt2_grid.copy())
            
        if t % 500 == 0:
            rprint(t)
            
        if t % 11000 == 0:
            break
    
    t2 = time.time()

    #### ANSWERS #####

    part_one = reduce(mul, quad_sums, 1)
    log_answers(part_one, "#", t0, t1, t2)
    
#### FUNCTIONS #####

def quad_coords(w, h):
    
    qc = ((0, int(h/2), 0, int(w/2)),
          (0, int(h/2), int((w/2)+1), w),
          (int((h/2)+1), h, 0, int(w/2)),
          (int((h/2)+1), h, int((w/2)+1), w))
    
    return qc

def symmetry_score(grid):
    w, h = len(grid[0]), len(grid)
    qc = quad_coords(w, h)[0:2]
    quads_tl_tr = [[row[x0:x1] for row in grid[y0:y1]] for (y0, y1, x0, x1) in qc]
    quad_tl = quads_tl_tr[0]
    w1, h1 = len(quad_tl[0]), len(quad_tl)
    quad_tr_reversed = [row.copy() for row in quads_tl_tr[1]]
    [row.reverse() for row in quad_tr_reversed]
    
    symmetry_grid = [[True if (quad_tl[j][i] == 1) and (quad_tr_reversed[j][i] == 1) else False for j in range(h1)] for i in range(w1)]
    
    return matrix_sum(symmetry_grid)
    # if quads_tl_tr[0] == quad_tr_reversed:
    #     show_arr(pt2_grid)
####

if __name__ == '__main__':
    run()