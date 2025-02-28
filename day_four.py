from lib import *
import numpy as np

def run():

    #### SETUP #####

    lines = read_lines(get_filename())
    matrix = [[c for c in line.strip('\n')] for line in lines]

    padding_amount = 4

    padding = ['#']*padding_amount
    padding_rows = [['#']*(len(matrix[0])+(2*padding_amount))]*padding_amount
    padded_matrix = padding_rows + [padding + row + padding for row in matrix] + padding_rows

    w, h = len(padded_matrix[0]), len(padded_matrix)

    #### PART ONE #####

    xmas_counts = np.zeros([w, h])

    for i in range(0, w):
        for j in range(0, h):
            
            if padded_matrix[j][i] == "X":
                n_xmas = get_n_xmas(padded_matrix, i, j)
                
                if n_xmas != 0:
                    xmas_counts[i, j] = n_xmas

    #### PART TWO #####

    crossmas_counts = np.zeros([w, h])

    for i in range(0, w):
        for j in range(0, h):
            
            if padded_matrix[j][i] == "A":
                n_crossmas = get_n_crossmas(padded_matrix, i, j)

                if n_crossmas != 0:
                    crossmas_counts[i, j] = n_crossmas
                    
    #### ANSWERS #####

    part_one = int(xmas_counts.sum())
    part_two = int(crossmas_counts.sum())
    
    log_answers(part_one, part_two)

#### FUNCTIONS #####

def get_n_xmas(matrix, x, y):
    
    xmas = ['X', 'M', 'A', 'S']
    directions = get_2D_surrounding_coords()
    directions.remove((0,0))
    
    n_xmas = 0

    for (dx, dy) in directions:
        for i in range(1, 4):
                      
            if matrix[y + (i*dy)][x + (i*dx)] != xmas[i]:
                break
            
            if i == 3:
                n_xmas += 1
                
    return n_xmas
            
def get_n_crossmas(matrix, x, y):
    
    ms = ['M', 'S']
    directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]

    for i, (dx, dy) in enumerate(directions):
                    
        if matrix[y + dy][x + dx] not in ms:
            break

        j = ms.index(matrix[y + dy][x + dx])
        if matrix[y - dy][x - dx] != ms[j-1]:
            break
        
        if i == 3:
            return 1

    return 0

####

if __name__ == '__main__':
    run()