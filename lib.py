import sys
import os
from rich import print as rprint
import itertools
import numpy as np
import math
import cv2

def get_filename():
    
    try:
        
        filename = sys.argv[1]
        
        os.path.isfile(filename)
        
        if os.path.isfile(filename) is not True:
            raise FileNotFoundError("File not specified does not exist")
        
    except IndexError as err:
        
        print(err)
    
    return sys.argv[1]

def read_lines(filename):
    
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    
    return lines

def read_sections(filename):
    
    with open(filename) as f:
        lines = f.readlines()
        
    lines = [line.strip() for line in lines]
    sections = [list(y) for x, y in itertools.groupby(lines, lambda z: z == "") if not x]
        
    return sections

def read_char_map(filename, to_int=False, pad_char=None):
    
    with open(filename) as f:
        if to_int:
            char_map = [[int(c) for c in line.strip()] for line in f.readlines()]
        else:
            char_map = [[c for c in line.strip()] for line in f.readlines()]
            
        if pad_char is not None:
            
            [row.insert(0, pad_char) for row in char_map]
            [row.append(pad_char) for row in char_map]
            char_map.insert(0, [pad_char]*len(char_map[0]))
            char_map.append([pad_char]*len(char_map[0]))
    
    return char_map
    
def log_answers(part_one, part_two, t0, t1, t2):
    
    p1_time = round(t1-t0, 5)
    p2_time = round(t2-t1, 5)
    rprint("Part one: {} ({})".format(part_one, p1_time))
    rprint("Part two: {} ({})".format(part_two, p2_time))
    
def get_2D_surrounding_coords():
    
    return [(dx, dy) for (dx, dy) in itertools.product(range(-1, 2), repeat=2)]

def map_to_coords(map):
    
    np_map = np.array(map)
    coords = np.argwhere(np_map).tolist()
    return coords

def blank_map(w, h, x=0):
    return[[x for _ in range(w)] for _ in range(h)]

def union_map(maps):
    
    if isinstance(maps, dict):
        arb_map = next(iter(maps.values()))
        w, h = len(arb_map[0]), len(arb_map)
        union = [[1 if any([maps[k][j][i] for k in maps]) else 0 for i in range(w)] for j in range(h)]
        
    if isinstance(maps, list):
        arb_map = maps[0]
        w, h = len(arb_map[0]), len(arb_map)
        union = [[1 if any([map[j][i] for map in maps]) else 0 for i in range(w)] for j in range(h)]
        
    return union
    
def matrix_sum(matrix):
    return sum([x for row in matrix for x in row])

def indices_dict(list):
    
    # Optimized dictionary creation
    indices_dict = {}
    for index, value in enumerate(list):
        if value not in indices_dict:
            indices_dict[value] = index

    return indices_dict

def get_digit(number, n):
    return number // 10**n % 10

def num_digits(number):
    if number > 0:
        digits = int(math.log10(number))+1
    elif number == 0:
        digits = 1
    return digits

def find_regions_as_arrays(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    region_arrays = []
    
    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and matrix[r][c] and not visited[r][c]
    
    def dfs(r, c, region_array):
        # Perform DFS to mark all connected cells
        stack = [(r, c)]
        while stack:
            x, y = stack.pop()
            if not visited[x][y]:
                visited[x][y] = True
                region_array[x][y] = True
                # Check only 4 directions: N, S, E, W
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if is_valid(x + dr, y + dc):
                        stack.append((x + dr, y + dc))
    
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] and not visited[r][c]:
                # Start a new region as an empty 2D array
                region_array = [[False] * cols for _ in range(rows)]
                dfs(r, c, region_array)
                region_arrays.append(region_array)
    
    return region_arrays

def find_regions_as_local_arrays(matrix):
    rows, cols = len(matrix), len(matrix[0])
    visited = [[False] * cols for _ in range(rows)]
    local_regions = []

    def is_valid(r, c):
        return 0 <= r < rows and 0 <= c < cols and matrix[r][c] and not visited[r][c]

    def dfs(r, c):
        # Perform DFS to mark all connected cells and find bounding box
        stack = [(r, c)]
        region_cells = []
        min_row, max_row, min_col, max_col = rows, -1, cols, -1
        while stack:
            x, y = stack.pop()
            if not visited[x][y]:
                visited[x][y] = True
                region_cells.append((x, y))
                # Update bounding box
                min_row = min(min_row, x)
                max_row = max(max_row, x)
                min_col = min(min_col, y)
                max_col = max(max_col, y)
                # Check only 4 directions: N, S, E, W
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    if is_valid(x + dr, y + dc):
                        stack.append((x + dr, y + dc))
        return region_cells, min_row, max_row, min_col, max_col

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] and not visited[r][c]:
                # Perform DFS and get region cells and bounding box
                region_cells, min_row, max_row, min_col, max_col = dfs(r, c)
                # Create submatrix for the region with bounding False area
                region_height = max_row - min_row + 1
                region_width = max_col - min_col + 1
                region_array = [[False] * (region_width + 2) for _ in range(region_height + 2)]
                for x, y in region_cells:
                    region_array[x - min_row + 1][y - min_col + 1] = True
                local_regions.append(region_array)

    return local_regions

def extended_gcd(a, b):
    """
    Perform the extended Euclidean algorithm.
    Returns gcd(a, b), and coefficients x, y such that a*x + b*y = gcd(a, b).
    """
    # Initial coefficients
    x0, y0 = 1, 0  # Coefficients for 'a'
    x1, y1 = 0, 1  # Coefficients for 'b'

    # Iterative process to find gcd and coefficients
    while b != 0:
        q = a // b  # Quotient of a divided by b
        a, b = b, a % b  # Update a and b to next step in Euclidean algorithm

        # Update coefficients
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    # At this point, a contains gcd(a, b), and (x0, y0) are the coefficients
    gcd = a
    return a, x0, y0

def show_arr(lists):
    image = np.uint8(np.array(lists))
    image = image/(image.max()/255.0)
    imS = cv2.resize(image, (600, 600))   
    cv2.imshow("x", imS)
    cv2.waitKey(0)

def matrix_max(matrix):
    
    mmax = 0
    
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if matrix[j][i] > mmax:
                mmax = matrix[j][i]
                
    return mmax


def find_char(grid, char):
    
    for j, row in enumerate(grid):
        for i, x in enumerate(row):
            if x == char:
                return (i, j)
            
def char_bool_map(grid, char):
    
    return [[x == "#" for x in row] for row in grid]

def map_visualiser(bool_maps_dict, extra_char_dict=None):
    
    any_map = list(bool_maps_dict.values())[0]
    w, h = len(any_map[0]), len(any_map)
    
    vis_grid = [["." for _ in range(w)] for _ in range(h)]

    for j in range(h):
        for i in range(w):
            for k in bool_maps_dict:
                if bool_maps_dict[k][j][i]:
                    vis_grid[j][i] = k
                    break
                
    if extra_char_dict is not None:
        for k in extra_char_dict:
            (i, j) = extra_char_dict[k]
            rprint(i, j)
            vis_grid[j][i] = k
                
    
    rprint(vis_grid)
        
    print("--------------------------------------------------")
    
def tab_print(grid, bool_grid, sec_bool=None):
    
    for j, row in enumerate(grid):
        for i, item in enumerate(row):
            if bool_grid[j][i]:
                if sec_bool is not None:
                    if sec_bool[j][i] is not False:
                        f = "[red]{}[/red]".format(sec_bool[j][i])
                        rprint(f, end='\t')
                    else:
                        rprint("#", end='\t')
            else:
                rprint(item, end='\t')
        rprint('\n')