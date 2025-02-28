from lib import *
import time
import itertools
from rich.progress import track

def run():

    #### SETUP #####

    sections = [line.split() for line in read_lines(get_filename())]
    targets = [int(section.pop(0).strip(":")) for section in sections]
    num_list = [[int(x) for x in nums] for nums in sections]
    
    t0 = time.time()

    #### PART ONE & TWO #####

    scores = []

    for i in track(range(0, len(targets)), description="Processing..."):
        
        n = len(num_list[i])
        operations_permutations = [list(i) for i in itertools.product([0, 1, 2], repeat=n-1)]

        for perm in operations_permutations:
            running_total = num_list[i][0]
            
            for j in range(n-1):
                running_total = operation(running_total, num_list[i][j+1], perm[j])
                if running_total > targets[i]: break
            
            if (running_total == targets[i]) & (j == n-2):
                scores.append((targets[i], perm))
                break
    
    t1 = time.time()    
    t2 = time.time()

    #### ANSWERS #####

    part_one = sum([score[0] for score in scores if 2 not in score[1]])
    part_two = sum([score[0] for score in scores])
    
    log_answers(part_one, part_two, t0, t1, t2)
    
#### FUNCTIONS #####

def operation(n1, n2, op):
    
    if op == 0: # ADDITION
        return n1+n2
    elif op == 1: # MULTIPLICATION
        return n1*n2
    else: # CONCATENATION
        return int(str(n1)+str(n2))

####

if __name__ == '__main__':
    run()