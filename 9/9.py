#!/usr/bin/env python

import re
from itertools import permutations

def do(input_file):
    with open(input_file) as f:
        strings = [s.strip() for s in f.readlines()]
    places = set()
    distances = dict()
    routes = dict()
    for s in strings:
        origin, destination, distance = re.match(r"(\w+) to (\w+) = (\d+)", s).groups()
        places.update([origin, destination])
        distances[(origin, destination)] = int(distance)
        distances[(destination, origin)] = int(distance)
    # for larger problem sets -> build graph and use Dijkstra
    min_distance, max_distance = 10000000, 0
    max_distance = 0
    for p in permutations(places):
       if len(p) == len(places):
           this_distance = sum([distances[od] for od in zip(p, p[1:])])
           min_distance = min(min_distance, this_distance)
           max_distance = max(max_distance, this_distance)
    print "shortest", min_distance
    print "longest", max_distance

do('input-test')
do('input')
