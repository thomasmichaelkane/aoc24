from lib import *

#### SETUP #####
 
lines = read_lines(get_filename())

left_list, right_list = [], []

for line in lines:
    left_list.append(int(line.split()[0])), right_list.append(int(line.split()[1]))

#### PART ONE #####

left_list.sort(), right_list.sort()
differences_list = [abs(x-y) for (x, y) in zip(left_list, right_list)]

#### PART TWO #####

scores = [right_list.count(x)*x for x in left_list]

#### ANSWERS #####

part_one = sum(differences_list), part_two = sum(scores)
log_answers(part_one, part_two)