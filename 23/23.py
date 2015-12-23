#!/usr/bin/env python27

import re

def run(input_file, a=0):
    with open(input_file) as f:
        program = [re.match(r"(\w+) ([-+\w]+)(?:, ([-+\w]+))?", s.strip()).groups() for s in f.readlines()]
    r = {'a': a, 'b': 0}
    pc = 0
    while pc < len(program):
        instruction, op1, op2 = program[pc]
        if instruction== 'inc':
            r[op1] += 1
        elif instruction == 'tpl':
            r[op1] *= 3
        elif instruction == 'hlf':
            r[op1] /= 2
        elif instruction == 'jmp':
            pc += int(op1)
            continue
        elif instruction == 'jie':
            if r[op1] % 2 == 0:
                pc += int(op2)
                continue
        elif instruction == 'jio':
            if r[op1] == 1:
                pc += int(op2)
                continue
        pc += 1
    print r['b']
    
#run('input-test')
run('input')
run('input', 1)
