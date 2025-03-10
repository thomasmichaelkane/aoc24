from .utils import *
import time

def run(as_example):

    #### SETUP #####
    
    lines = read_lines(get_filename("1", as_example))

    left_list, right_list = [], []

    for line in lines:
        left_list.append(int(line.split()[0])), right_list.append(int(line.split()[1]))

    t0 = time.time()
    
    #### PART ONE #####

    left_list.sort(), right_list.sort()
    differences_list = [abs(x-y) for (x, y) in zip(left_list, right_list)]

    t1 = time.time()
    
    #### PART TWO #####

    scores = [right_list.count(x)*x for x in left_list]

    t2 = time.time()
    
    #### ANSWERS #####

    part_one, part_two = sum(differences_list), sum(scores)
    log_answers(part_one, part_two, t0, t1, t2)
    
if __name__ == '__main__':
    run()