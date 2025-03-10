from .utils import *
import time

def run(as_example=False):
  
    #### SETUP ####

    sections = read_sections(get_filename("19", as_example))
    towels = [x.strip() for x in sections[0][0].split(",")]
    arrangements = sections[1]
    towels.sort(reverse=True), arrangements.sort(reverse=True)
    # towels.sort(), arrangements.sort()

    
    # rprint(towels)
    # rprint(arrangements)
    
    t0 = time.time()

    #### PART ONE #####
    
    towel_base_dict = {"b": 1, "g": 2, "r": 3, "u": 4, "w": 5}
    towels5 = {towel: convert_base5(towel, towel_base_dict) for towel in towels}
    arrangements5 = {arrangement: convert_base5(arrangement, towel_base_dict) for arrangement in arrangements}
    
    rprint(towels5)
    rprint(arrangements5)
    
    test_arr = [21]
    
    possibles = []
    
    for i in range(0, len(test_arr)):
        
        if i == 0:
            
            for k in towels5:
                
                rprint(k)
                
                n = len(k)
                
                rprint(n)
                
                test_t = towels5[k] * (10**i)
                
                rprint("t", test_t)
                
                test_a = (test_arr[0]) % (10**(i + n))
                
                rprint("a", test_a)
            
                if test_t == test_a:
                
                    possibles.append([k])
    
        # for t in towels5:
        
    rprint(possibles)
            
            
    
    
    

    
    
    
    # for towel in towels:
    #     for c in towel
    
    
    # 002140  
    # 0 + 20 + 50 + 1000 = 1070
    
    
    
    
    
    t1 = time.time()

    #### PART TWO #####

    #todo
    
    t2 = time.time()

    #### ANSWERS #####

    # log_answers(part_one, part_two, t0, t1, t2)
    
#### FUNCTIONS #####

def convert_base5(characters, dict):
    
    base10 = 0
    
    for i in reversed(range(len(characters))):
        
        base10 += ((10**i) * dict[characters[i-1]])
        
    return base10

####

if __name__ == '__main__':
    run()