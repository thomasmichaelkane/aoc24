from .utils import *
import time

def run(as_example=False):

    #### SETUP #####

    lines = read_lines(get_filename("2", as_example))
    reports = [[int(x) for x in line.split()] for line in lines]

    t0 = time.time()

    #### PART ONE #####

    report_differences = [[report[i] - report[i+1] for i in range(len(report) - 1)] for report in reports]
    safety_checks = [check_safety(report) for report in report_differences]

    t1 = time.time()

    #### PART TWO #####

    dampened_checks = []

    for i, check in enumerate(safety_checks):
        
        if check is True:
            dampened_checks.append(check)
            
        else:
            dampened_checks.append(check_dampened_safety(reports[i]))
            
    t2 = time.time()
            
    #### ANSWERS #####

    part_one = safety_checks.count(True)
    part_two = dampened_checks.count(True)

    log_answers(part_one, part_two, t0, t1, t2)
    
#### FUNCTIONS #####

def check_safety(report):
    
    max_difference = 3
        
    if all((d > 0) & (abs(d) <= max_difference) for d in report):
        # descending and safe
        return True
        
    elif all((d < 0) & (abs(d) <= max_difference) for d in report):
        # ascending and safe
        return True
        
    else:
        # unsafe
        return False
    
def check_dampened_safety(report):
    
    for i in range(len(report)):
        
        dampened_report = report.copy()
        dampened_report.pop(i)
        dampened_diff = [dampened_report[i] - dampened_report[i+1] for i in range(len(dampened_report) - 1)]

        if check_safety(dampened_diff):
            return True
        
    return False

if __name__ == '__main__':
    run()