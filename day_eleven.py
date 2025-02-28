from lib import *
import time
import matplotlib.pyplot as plt
from collections import Counter

def run():

    #### SETUP #####

    stones = [int(x) for x in read_lines(get_filename())[0].split()]
    
    # stones = [0]
    
    n_blinks = int(sys.argv[2])
    
    print(stones)
    
    t0 = time.time()

    #### PART ONE #####

    #todo
    
    def blink(stones):
        
        i = 0
    
        while i < len(stones):
            
            n_digits = num_digits(stones[i])
            
            if stones[i] == 0:
                stones[i] = 1
                i += 1
            elif n_digits % 2 != 0:  # odd numbers  
                stones[i] = stones[i]*2024
                i += 1
            else: # n_digits % 2 == 0: # even 
                stone_string = str(stones[i])
                stones[i] = int(stone_string[:int(len(stone_string)/2)])
                stones.insert(i+1, int(stone_string[int(len(stone_string)/2):]))
                

                i += 2
            
        return stones
    
    stone_lengths = []
    stones_unique = list(set(stones))
    
    for i in range(n_blinks):
        # rprint(stones)
        stones = blink(stones_unique)
        stones.sort()
        stones_dict = Counter(stones)
        stones_unique = list(set(stones))
        stones_unique.sort()
        rprint(stones)
        rprint(stones_dict)
        rprint(stones_unique)
        rprint("---------------")
        stone_lengths.append(len(stones))
        
    # rprint(stone_lengths)

    # plt.plot([(i, stone_lengths[i+1]/stone_lengths[i]) for i in range(len(stone_lengths)-1)])
        
        
    # plt.show()
    # for i in range(len(stone_lengths)):   
    #     rprint(stone_lengths[i])
    
    # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
    
    # If the stone is engraved with a number that has an even number of digits, 
    # it is replaced by two stones. The left half of the digits are engraved on the new left stone, 
    # and the right half of the digits are engraved on the new right stone. 
    # (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
    
    # If none of the other rules apply, the stone is replaced by a new stone; 
    # the old stone's number multiplied by 2024 is engraved on the new stone.
    
    t1 = time.time()

    #### PART TWO #####

    #todo
    
    t2 = time.time()

    #### ANSWERS #####
    
    part_one = len(stones)

    log_answers(part_one, "#", t0, t1, t2)
    
#### FUNCTIONS #####

def split_even_digits(large_int, n_digits):
    
    right_int = sum([(get_digit(large_int, i))*(10**i) for i in range(int(n_digits/2))])
    left_int = sum([(get_digit(large_int, i))*(10**i) for i in range(int(n_digits/2), int(n_digits))])

    return left_int, right_int

####

if __name__ == '__main__':
    run()