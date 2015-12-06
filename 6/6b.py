#!/usr/bin/env python

from collections import defaultdict
import re

def level_change(lights, x1, y1, x2, y2, change):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            lights[x][y] += change
            if lights[x][y] < 0:
                lights[x][y] = 0

def turn_it_off_and_on_again(input_file):
    with open(input_file) as f:
        instructions = [s.strip() for s in f.readlines()]
    lights = [[0] * 1000 for i in range(1000)]
    for instr in instructions:
        (what, x1, y1, x2, y2) = [int(m) if m[0] != 't' else m for m in re.match(r"^([\D]+) ([\d]+),([\d]+) through ([\d]+),([\d]+)$", instr).groups()]
        change = 1
        if what == 'turn off':
            change = -1
        elif what == 'toggle':
            change = 2
        level_change(lights, x1, y1, x2, y2, change)
    return sum([sum(y) for y in lights])
            
print turn_it_off_and_on_again('input-test-1')
print turn_it_off_and_on_again('input')
