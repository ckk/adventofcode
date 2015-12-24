#!/usr/bin/env python27

import re
from itertools import combinations

def do(input_file, group_count):
    with open(input_file) as f:
        packages = [int(s.strip()) for s in f.readlines()]
    group_weight = sum(packages) / group_count
    for i in range(2, 10): # assumption that smallest possible group is within this range
        possible_groups = [group for group in combinations(packages, i) if sum(group) == group_weight]
        if len(possible_groups) > 0:
            break
    # assumption: the smallest group possible with the smallest QE will still allow the rest of the
    # packages to be divided into two groups with the same total weight for the input
    print sorted([reduce(lambda x, y: x*y, g, 1) for g in possible_groups])[0]
    
#do('input-test', 3)
#do('input-test', 4)
do('input', 3)
do('input', 4)
