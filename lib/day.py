from .utils import *
import time

def run(as_example=False):
  
  #### SETUP ####

  lines = read_lines(get_filename("N", as_example))
  
  print(lines)
  
  t0 = time.time()
  
  #### PART ONE ####
  
  # part one logic
  
  t1 = time.time()

  #### PART TWO ####
  
  # part two logic
  
  t2 = time.time()
  
  #### ANSWERS ####

  part_one = None
  part_two = None

  log_answers(part_one, part_two, t0, t1, t2)
  
#### FUNCTIONS #####

# functions


if __name__ == '__main__':
  run()