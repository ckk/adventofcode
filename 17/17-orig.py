#!/usr/bin/env python

import re
from itertools import combinations

# first version, done late in the day CET, timed myself and due to a stupid mistake in the beginning
# both parts took 11:47, would have been around #57, if I had been fully awake at 6 am. :)

def do(input_file, amount):
    with open(input_file) as f:
        buckets = [int(s.strip()) for s in f.readlines()]
    combos = 0
    got_part_two = False
    for i in range(1, len(buckets)+1):
        combos_here = 0
        for c in combinations(buckets, i):
            if sum(c) == amount:
                combos += 1
                combos_here += 1
        if not got_part_two and combos_here > 0:
            got_part_two = True
            print combos_here
    print combos

do('input-test', 25)
do('input', 150)
