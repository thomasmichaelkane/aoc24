from lib import *
import time

def run():

    #### SETUP #####

    [rules_str, page_numbers_str] = read_sections(get_filename())
    
    rules = [[int(r) for r in string.split('|')] for string in rules_str]
    page_numbers = [[int(p) for p in string.split(',')] for string in page_numbers_str]

    s = set(r[0] for r in rules)
    
    after = {}
    before = {}

    for n in s:
        after[n] = set(k[1] for k in rules if k[0] == n)
        before[n] = set(j[0] for j in rules if j[1] == n)
        
    t0 = time.time()
                
    #### PART ONE #####

    valid_pages_middle = []
    valid_pages_id = []
    
    for i2, p in enumerate(page_numbers):
        for i, n in enumerate(p):
            if not (all(j in before[n] for j in p[0:i]) and all(k in after[n] for k in p[i+1:])):
                break
            
            if i == len(p)-1:
                valid_pages_middle.append(p[int(len(p)/2)])
                valid_pages_id.append(i2)
                
    t1 = time.time()
            
    #### PART TWO #####
    
    problem_updates = [p for i, p in enumerate(page_numbers) if i not in valid_pages_id]
    
    p_middle = []
    
    for update in problem_updates:
        for n in update:
            trial = update.copy()
            trial.remove(n)
            if len([j for j in trial if j in before[n]]) == len([k for k in trial if k in after[n]]):
                p_middle.append(n)
                break
            
    t2 = time.time()
            
    #### ANSWERS #####

    part_one = sum(valid_pages_middle)
    part_two = sum(p_middle)
    
    log_answers(part_one, part_two, t0, t1, t2)
    
#### FUNCTIONS #####

####

if __name__ == '__main__':
    run()