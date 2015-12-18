#!/usr/bin/env python

from __future__ import print_function
from copy import deepcopy
from itertools import ifilter, product, repeat

def neighbors(grid, x, y):
    result = list()
    for nx in range(max(0, x-1), min(x+2, len(grid[0]))):
        for ny in range(max(0, y-1), min(y+2, len(grid))):
            if not (nx == x and ny == y):
                yield grid[ny][nx]

def life(input_file, generations, stuck=False):
    with open(input_file) as f:
        grid = [[True if c == '#' else False for c in row.strip()] for row in f.readlines()]
    if stuck:
        grid[0][0], grid[0][-1],  grid[-1][0], grid[-1][-1] = True, True, True, True
    for g in range(generations):
        newgrid = deepcopy(grid) 
        for x in range(len(grid[0])):
            for y in range(len(grid)):
                nc = 0
                for n in neighbors(grid, x, y):
                    if n:
                        nc += 1
                        if nc > 3:
                            break
                newgrid[y][x] = (grid[y][x] and 2 <= nc <= 3) or (not grid[y][x] and nc == 3)
        grid = newgrid
        if stuck:
            grid[0][0], grid[0][-1],  grid[-1][0], grid[-1][-1] = True, True, True, True
    print("lights: %d" % sum([row.count(True) for row in grid]))
                
life('input-test', 4)
life('input-test', 5, stuck=True)
life('input', 100)
life('input', 100, stuck=True)
