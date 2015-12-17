#!/usr/bin/env python

import re
from itertools import combinations

# More clever version, or at least shorter :)

def do(input_file, amount):
    with open(input_file) as f:
        buckets = [int(s.strip()) for s in f.readlines()]
    combo_sums = [len([c for c in combinations(buckets, n) if sum(c) == amount]) for n in range(1, len(buckets)+1)]
    print sum(combo_sums)
    print next(s for s in combo_sums if s > 0)

do('input-test', 25)
do('input', 150)
