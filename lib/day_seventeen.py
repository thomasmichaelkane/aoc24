from .utils import *
import time
from rich.progress import track
import matplotlib.pyplot as plt

def run(as_example=False):
  
    #### SETUP ####

    sections = read_sections(get_filename("17", as_example))
    
    registers = {"A": get_register_value(sections[0][0]),
                 "B": get_register_value(sections[0][1]),
                 "C": get_register_value(sections[0][2])}
    
    
    instructions = [int(x) for x in 
                    (sections[1][0].split()[1]).split(",")]
    
    # instructions_as_int = int("".join([str(x) for x in instructions]))
    
    rprint(instructions)
    
    t0 = time.time()

    #### PART ONE #####

    outputs = []
    ip = 0
    
    num_instructions = len(instructions)
    
    while ip < num_instructions:
        
        ip = advance_program(instructions, 
                             ip, 
                             registers, 
                             outputs)
    
    # rprint(outputs)
    part_one = ",".join([str(x) for x in outputs])
    
    t1 = time.time()

    #### PART TWO #####

    match_lengths, match_lengths_indices = [], []
    
    start = 2**(45)
    end = 2**(48)
    
    # first significant match
    i = 35184372099626
    # i = 35184731236906
    
    # significant match repitition gaps
    jumps = [3, 2, 524283]
    # jumps = [3, 2, 134217723]
    
    
    # index of last possible match
    last = 469_766_528
    
    num_instructions = len(instructions)
    
    for j in track(range(last-int(last/5000), last)):
        
        i = i + jumps[j%3]

        registers = {"A": i, "B": 0, "C": 0}
        
        outputs, ip = [], 0
        
        while ip < num_instructions:
            
            ip = advance_program(instructions, 
                                ip, 
                                registers, 
                                outputs)
            
            if outputs != instructions[0:len(outputs)]:
                # if len(outputs) >= 10:
                match_lengths.append(len(outputs))
                match_lengths_indices.append(i)
                break
            
        if outputs == instructions:
            rprint("EUREKA!", i)
            break
    
    # rprint(match_lengths)
    plt.scatter(range(0, len(match_lengths)), match_lengths)
    plt.show()
    
    match_lengths_diff = [match_lengths_indices[i+1] - match_lengths_indices[i] for i in range(len(match_lengths_indices)-1)]
    # rprint(match_lengths)
    # rprint(match_lengths_diff)
    
    t2 = time.time()

    #### ANSWERS #####

    log_answers(part_one, "#", t0, t1, t2)
    
#### FUNCTIONS #####

def get_register_value(string):
    return int(string.split()[2])

def advance_program(instructions, ip, registers, outputs):
    
    opcode, operand = instructions[ip], instructions[ip+1]
    jump = False
    
    opcode_dict = {0: "adv",
                   1: "bxl",
                   2: "bst",
                   3: "jnz",
                   4: "bxc",
                   5: "out",
                   6: "bdv",
                   7: "cdv"}
    
    # rprint(opcode_dict[opcode], operand)

    match opcode:
        case 0: # adv ->  div regA/ 2**combo-op (int then -> A)
            registers["A"] = exp_div(registers["A"], combo(operand, registers))
            
        case 1: # bxl -> bitwise XOR regB and lit op (-> B)
            registers["B"] = xor(registers["B"], operand)
            
        case 2: # bst - combo-op modulo 8 (-> B)
            registers["B"] = mod8(combo(operand, registers))
            
        case 3: # jnz -> jump if A != 0
            if registers["A"] != 0: jump = True
            
        case 4: # bxc -> bitwise XOR regB and regC (-> B)
            registers["B"] = xor(registers["B"], registers["C"])
            
        case 5: # out -> combo-op modulo 8 (-> outputs)
            outputs.append(mod8(combo(operand, registers)))
            
        case 6: # bdv -> div regA/ 2**combo-op (int then -> B)
            registers["B"] = exp_div(registers["A"], combo(operand, registers))
            
        case 7: # cdv -> div regA/ 2**combo-op (int then -> C)
            registers["C"] = exp_div(registers["A"], combo(operand, registers))

    if jump: 
        ip = operand
    else: 
        ip += 2
        
    return ip

def xor(a, b):
    return a ^ b

def exp_div(n, exp):
    return int(n/(2**exp))

def mod8(a):
    return a % 8


def combo(operand, registers):
    
    match operand:
        case 0 | 1 | 2 | 3:
            return operand
        case 4:
            return registers["A"]
        case 5:
            return registers["B"]
        case 6:
            return registers["C"]
        case _:
            rprint("invalid operand")
            return None

####

if __name__ == '__main__':
    run()