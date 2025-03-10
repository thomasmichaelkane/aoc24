from .utils import *
import time

def run(as_example=False):

    #### SETUP ####

    lines = read_lines(get_filename("6", as_example))

    start_chars = ['^', '>', 'v', '<']
    movement = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    obstacles_map = [[x == "#" for x in line.strip()] for line in lines]
    travelled_map = [[0]*len(obstacles_map[0]) for _ in range(len(obstacles_map))]

    (x0, y0), d0 = find_start(lines, start_chars)
    (dx0, dy0) = movement[d0]

    w, h = len(obstacles_map[0]), len(obstacles_map)

    t0 = time.time()

    #### PART ONE #####

    x, y, dx, dy, direction = x0, y0, dx0, dy0, d0
    travelled_map[y][x] = 1

    while (x+dx >= 0) and (y+dy >= 0) and (x+dx < w) and (y+dy < h):

        if obstacles_map[y+dy][x+dx]:
            direction += 1
            (dx, dy) = movement[direction % len(movement)]

        x, y = x + dx, y + dy
        travelled_map[y][x] = 1

    t1 = time.time()
    part_one = sum([sum(row) for row in travelled_map])

    #### PART TWO #####

    travelled = [(i, j) for i in range(len(travelled_map)) for j in range(len(travelled_map)) if travelled_map[j][i]]
    travelled.remove((x0, y0))
    loop_n = 0

    for (i, j) in travelled:

            obstacles_map = [[x == "#" for x in line.strip()] for line in lines]
            travelled_map = [[-1]*len(obstacles_map[0]) for _ in range(len(obstacles_map))]

            x, y, dx, dy, direction = x0, y0, dx0, dy0, d0
            obstacles_map[j][i] = True

            while (x+dx >= 0) and (y+dy >= 0) and (x+dx < w) and (y+dy < h):

                if obstacles_map[y+dy][x+dx]:
                    while obstacles_map[y+dy][x+dx]:
                        direction = (direction + 1) % len(movement)
                        (dx, dy) = movement[direction]


                if travelled_map[y][x] == direction:
                    loop_n += 1
                    break
                else:
                    travelled_map[y][x] = direction

                x, y = x + dx, y + dy


    t2 = time.time()
    part_two = loop_n

    #### ANSWERS #####

    log_answers(part_one, part_two, t0, t1, t2)
    
#### FUNCTIONS #####

def find_start(lines, start_chars):
    
    for j, line in enumerate(lines):
        for i, char in enumerate(line):
            if char in start_chars:
                return (i, j), start_chars.index(char)
            
def map_visualiser(map, char, second_map, second_char):
    
    for j in range(len(map)):
        vis_row = []
        for i in range(len(map[0])):
            if map[j][i] != -1:
                vis_row.append(char)
            elif second_map[j][i]:
                vis_row.append(second_char)
            else:
                vis_row.append(".")
                
        rprint(vis_row)
        
    print("--------------------------------------------------")
    
####

if __name__ == '__main__':
    run()