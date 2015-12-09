#!/usr/bin/env python

import re
from itertools import permutations

def calc_distance(path_tuple, distances):
    path = list(path_tuple)
    cost = 0
    a = path.pop(0)
    while len(path) > 0:
        b = path.pop(0)
        cost += distances[(a, b)]
        a = b
    return cost

def do(input_file):
    with open(input_file) as f:
        strings = [s.strip() for s in f.readlines()]
    places = set()
    distances = dict()
    routes = dict()
    for s in strings:
        origin, destination, distance = re.match(r"(\w+) to (\w+) = (\d+)", s).groups()
        places.add(origin)
        places.add(destination)
        distances[(origin, destination)] = int(distance)
        distances[(destination, origin)] = int(distance)
    # for larger problem sets -> build graph and use Dijkstra
    place_count = len(places)
    min_distance = 10000000
    max_distance = 0
    min_path = ("N/A")
    max_path = ("N/A")
    for p in permutations(places):
       if len(p) == place_count:
           this_distance = calc_distance(p, distances)
           if this_distance < min_distance:
               min_distance = this_distance
               min_path = p
           if this_distance > max_distance:
               max_distance = this_distance
               max_path = p
    print "shortest", min_path, min_distance
    print "longest", max_path, max_distance

do('input-test')
do('input')
