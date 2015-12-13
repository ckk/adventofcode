#!/usr/bin/env python

import re
from itertools import permutations

def do(input_file, me=False):
    with open(input_file) as f:
        strings = [s.strip() for s in f.readlines()]
    people = set()
    happiness = dict()
    for s in strings:
        a, pos_neg, happy_units, b = re.match(r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)", s).groups()
        people.update([a, b])
        happy_units = int(happy_units)
        if pos_neg == 'lose':
            happy_units = -happy_units
        happiness[(a, b)] = happy_units
    if me:
        for p in people:
            happiness[('me', p)] = 0
            happiness[(p, 'me')] = 0
        people.add('me')
    max_happy = 0
    for t in permutations(people):
       this_happy = 0
       for i in range(len(t)):
           right = (i+1) % len(t)
           this_happy += happiness[(t[i], t[right])]
           this_happy += happiness[(t[right], t[i])]
       max_happy = max(max_happy, this_happy)
    print "maximum happiness:", max_happy

do('input-test')
do('input')
do('input', True)
