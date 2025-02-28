from lib import *
import re

def run():

    #### SETUP #####

    string = "".join(read_lines(get_filename()))

    #### PART ONE #####

    mul_matches = find_operation_regex(string)
    mul_operations = [get_digits(match) for match in mul_matches]
    scores = [x*y for (x,y) in mul_operations]

    #### PART TWO #####

    dos, donts = find_do_dont_regex(string)
    deactivated = find_deactivated_sections(dos, donts)

    string_as_list = list(string)
            
    for (start, end) in deactivated:
        for i in range(start, end):  
            string_as_list[i] = "#"

    mod_string = "".join(string_as_list)
        
    mul_matches = find_operation_regex(mod_string)
    mul_operations = [get_digits(match) for match in mul_matches]
    updated_scores = [x*y for (x,y) in mul_operations]

    #### ANSWERS #####

    part_one = sum(scores)
    part_two = sum(updated_scores)

    log_answers(part_one, part_two)


#### FUNCTIONS #####

def find_operation_regex(string):
    
    regex = r"mul\([0-9]+,[0-9]+\)"
    
    matches = re.findall(regex, string)

    return matches

def get_digits(match):
    
    regex = r"[0-9]+"
    
    digits = re.findall(regex, match)
    ints = [int(d) for d in digits]
    
    return ints

def find_do_dont_regex(string):
    
    do_regex = r"do\(\)"
    dont_regex = r"don't\(\)"
    
    dos = re.finditer(do_regex, string)
    dos_indices = [d.start() for d in dos]
    
    donts = re.finditer(dont_regex, string)
    donts_indices = [d.start() for d in donts]

    return dos_indices, donts_indices

def find_deactivated_sections(dos, donts):
    
    deactivated_sections = []

    for dont in donts:
        for do in dos:
            if do > dont:
                break
        
        deactivated_sections.append([dont, do])
        
    return deactivated_sections

if __name__ == "__main__":
    run()