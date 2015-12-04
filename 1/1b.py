#!/usr/bin/env python

floor = 0
index = 0
basement = 0
with open("input") as f:
    input = f.read().strip()
    for c in input:
        index +=1
        if c == '(':
           floor += 1
        if c == ')':
           floor -= 1
        if floor < 0 and basement == 0:
           basement = index
    print "Floor: %d, basement index: %d" % (floor, basement)
