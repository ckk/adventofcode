#!/usr/bin/env python

from collections import defaultdict
import re

def on_off(lights, x1, y1, x2, y2, val):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            lights[x][y] = val

def toggle(lights, x1, y1, x2, y2):
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            lights[x][y] = not lights[x][y]

def turn_it_off_and_on_again(input_file):
    with open(input_file) as f:
        instructions = [s.strip() for s in f.readlines()]
    lights = [[False] * 1000 for i in range(1000)]
    for instr in instructions:
        (what, x1, y1, x2, y2) = [int(m) if m[0] != 't' else m for m in re.match(r"^([\D]+) ([\d]+),([\d]+) through ([\d]+),([\d]+)$", instr).groups()]
        if what == 'turn on':
            on_off(lights, x1, y1, x2, y2, True)
        elif what == 'turn off':
            on_off(lights, x1, y1, x2, y2, False)
        elif what == 'toggle':
            toggle(lights, x1, y1, x2, y2)
    return sum([y.count(True) for y in lights])
            
print turn_it_off_and_on_again('input-test-1')
print turn_it_off_and_on_again('input')
