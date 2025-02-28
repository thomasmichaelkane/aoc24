from lib import *
import time
from collections import Counter
from rich.progress import track

def run():

    #### SETUP #####

    disk = [int(x) for x in read_lines(get_filename())[0]]
    
    disk_data, disk_space = disk[::2], disk[1::2]
    
    disk_char = []
    
    for i in range(0, len(disk_data)):
        [disk_char.append(i) for _ in range(disk_data[i])]
        if i < len(disk_space) - 1:
            [disk_char.append(-1) for _ in range(disk_space[i])]
    
    print_disk(disk_char[:50])
    
    disk_char_data = [x for x in disk_char if x != -1]
    data_length = len(disk_char_data)
    
    t0 = time.time()

    #### PART ONE #####
    
    compacted_disk = []
    i, j = 0, 0
    
    disk_char_con = disk_char.copy()
    
    while len(compacted_disk) < data_length:
        
        if disk_char_con[i] == -1:
            empty = True
            while empty:
                bit = disk_char_con.pop()
                if bit != -1: empty = False
            
            j += 1   
            compacted_disk.append(disk_char_data[data_length-j])
            
            
        else:
            compacted_disk.append(disk_char_con[i])
            
        i += 1
    
    scores = [x*i for i, x in enumerate(compacted_disk)]
    
    t1 = time.time()

    #### PART TWO #####

    count_dict = dict(Counter(reversed(disk_char_data)))
    index_dict = indices_dict(disk_char)
    index_dict.pop(-1)
    
    for k, n in track(count_dict.items()):
        
        n_space = 0
    
        for i, x in enumerate(disk_char):
            
            if i == index_dict[k]:
                break
                
            if (n_space >= n):
                disk_char[(i-n):i] = [k]*n
                disk_char[index_dict[k]:index_dict[k]+n] = [-1]*n
                
                remove_endspace(disk_char)
                
                break
            
            if x == -1:
                n_space +=1
            else:
                n_space = 0
                
    print_disk(disk_char[:50])
    print_disk(disk_char[-50:])
                
    scores_pt2 = [(x, i, x*i) for i, x in enumerate(disk_char) if x != -1]
    print(scores_pt2[:50])

    t2 = time.time()

    #### ANSWERS #####

    part_one = sum(scores)
    part_two = sum([x[2] for x in scores_pt2])
    log_answers(part_one, part_two, t0, t1, t2)
    
#### FUNCTIONS #####

def print_disk(list):
    
    string_list = [str(x) if x != -1 else "." for x in list]
    string = "\\".join(string_list)
    rprint(string)
    
def remove_endspace(disk):
    
    while disk[-1] == -1:
        disk.pop()
        
    return disk

####

if __name__ == '__main__':
    run()