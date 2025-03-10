from .utils import *
import time
import itertools
from rich.progress import track
import math

def run(as_example=False):
  
    #### SETUP ####
    
    weight_A, weight_B = 3, 1

    games_info = [list(y) for x, y in itertools.groupby(read_lines(get_filename("13", as_example)), lambda z: z == "") if not x]
    games = [{"A": {"Units": get_x_and_y(info[0], 2), "weight": weight_A}, 
              "B": {"Units": get_x_and_y(info[1], 2), "weight": weight_B}, 
              "Prize": get_x_and_y(info[2], 1)} for info in games_info]
    
    print(games)
    
    t0 = time.time()

    #### PART ONE #####

    a, b, c = 1, 1, 1
    gcd, x, y = extended_gcd(a, b)
    x, y *= (c // gcd), (c // gcd)

    # Generate multiple solutions using the formula:
    # x = x0 + k * (b / gcd), y = y0 - k * (a / gcd)
    
    solutions = []
    # for k in range(-num_solutions // 2, num_solutions // 2 + 1):
    #     x = x0 + k * (b // gcd)
    #     y = y0 - k * (a // gcd)
    #     solutions.append((x, y))

    return solutions



    # brute force
    
    min_prices = []

    
    ## j = ((cx*ay/ax) - cy) / (bx*ay/ax)
    ## i = (cy - byj)/ay
    
    for game in games:
        
        rprint("--------------")
        rprint(math.gcd(game["A"]["Units"][0], game["B"]["Units"][0]))
        rprint(math.gcd(game["A"]["Units"][1], game["B"]["Units"][1]))
        
        rprint(game["A"]["Units"][0], game["B"]["Units"][0], extended_gcd(game["A"]["Units"][0], game["B"]["Units"][0]))
        rprint(game["A"]["Units"][1], game["B"]["Units"][1], extended_gcd(game["A"]["Units"][1], game["B"]["Units"][1]))
        
        # c = min([game["A"]["Units"][0], game["B"]["Units"][0]])
        # d = max([game["A"]["Units"][0], game["B"]["Units"][0]])

        # # i = 0

        # while True:
        #     i += 1
        #     r = c%d
        #     q = int(c/d)
            
        #     c = d
        #     d = r
            # if r == 0:
            #     break

    #     j = ((game["Prize"][0]*game["A"]["Units"][1])/game["A"]["Units"][0]) / ((game["B"]["Units"][0]*game["A"]["Units"][1])/game["A"]["Units"][0]) 
    #     i = (game["Prize"][1] - (game["B"]["Units"][1] * j)) / (game["A"]["Units"][1])
        
    #     # if (i > 0) and (j > 0):
    #     rprint(i, j)
    #     rprint(i*game["A"]["weight"] + j*game["B"]["weight"])
        
            
        
    # for game in track(games):
    #     min_price = 400
    #     for i in range(100):
    #         for j in range(100):
    #             # score = (game["A"][0]*i + game["B"][0]*j)
    #             score = (game["A"][0][0]*i + game["B"][0][0]*j, game["A"][0][1]*i + game["B"][0][1]*j)
    #             # rprint(score)
    #             if score == game["Prize"]:
    #                 # score correct
    #                 winning_price = (game["A"][1]*i + game["B"][1]*j)
    #                 if winning_price < min_price:
    #                     # new price is min
    #                     min_price = winning_price
                        
        # rprint(min_price)
        
        # if min_price != 400:
        #     min_prices.append(min_price)
                        
                
    
    t1 = time.time()

    #### PART TWO #####

    #todo
    
    
    ## A: ((ax, ay), 3), 'B': ((bx, by), 1), 'Prize': (cx, cy)},
    ## axi + bxj = cx
    ## ayi + byj = cy
    ## i = (cx - bxj)/ax
    ## ay*((cx - bxj)/ax) + byj = cy
    ## (cx*ay/ax) - (bx*ay/ax)j + byj = cy
    ## (bx*ay/ax)j = (cx*ay/ax) - cy
    
    ## j = ((cx*ay/ax) - cy) / (bx*ay/ax)
    ## i = (cy - byj)/ay
    
    ## axi + bxj = cx
    ## ayi + byj = cy
    
    # where a and b whole numebrs
    
    t2 = time.time()

    #### ANSWERS #####
    
    part_one = sum(min_prices)

    log_answers(part_one, "#", t0, t1, t2)
    
#### FUNCTIONS #####

def get_x_and_y(string, i):
    
    info = string.split()
    
    return int(info[i][2:].strip(",")), int(info[i+1][2:].strip(","))

if __name__ == '__main__':
    run()