#!/usr/bin/env python

import re
from itertools import ifilter, product, repeat

# a little bit of hardcoding here:
properties_gt = ('cats', 'trees')
properties_lt = ('pomeranians', 'goldfish')

# this is for part two only, did part one on the command line
def do(input_file_analysis, input_file_sues):
    with open(input_file_sues) as f:
        sue_strings = [s.strip() for s in f.readlines()]
    with open(input_file_analysis) as f:
        analysis_strings = [s.strip() for s in f.readlines()]
    sues = [dict(re.findall(r"(\w+): (\d+)[, ^:]*", s)) for s in sue_strings]
    analysis = dict([s.split(': ') for s in analysis_strings])
    scores = list()
    for sue in sues:
        score = 0
        for prop, value in analysis.iteritems():
            if prop in sue:
                if prop in properties_gt:
                    if sue[prop] > value:
                        score += 1
                    continue
                if prop in properties_lt:
                    if sue[prop] < value:
                        score += 1
                    continue
                if sue[prop] == value:
                    score += 1
        scores.append(score)
    print sorted(enumerate(scores), key=lambda x: x[1])[-1][0]+1
                
do('input-analysis', 'input-sues')
