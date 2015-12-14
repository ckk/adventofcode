#!/usr/bin/env python

import re
from collections import defaultdict

def do(input_file, seconds):
    with open(input_file) as f:
        strings = [s.strip() for s in f.readlines()]
    reindeer = dict()
    for s in strings:
        #Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
        name, speed, flying, resting = re.match(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.$", s).groups()
        reindeer[name] = (int(speed), int(flying), int(resting))
    reindeer_distances = dict()
    for rd in reindeer.keys():
       speed, flying, resting = reindeer[rd]
       full, remainder = divmod(seconds, flying + resting)
       reindeer_distances[rd] = speed * full * flying + speed * min(remainder, flying)
    return reindeer_distances

print max(do('input-test', 1000).values())
print max(do('input', 2503).values())
reindeer_points = defaultdict(lambda: 0)
# there might be a more clever way but I guesstimate this will only take less
# than a second so let's not prematurely optimize
for i in range(1, 2504):
    dists = do('input', i)
    max_points = max(dists.values())
    for rd in dists:
        if dists[rd] == max_points:
            reindeer_points[rd] += 1 
print max(reindeer_points.values())
