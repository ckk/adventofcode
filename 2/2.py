#!/usr/bin/env python

def box_sq_feet(b):
    area = sum([2 * a for a in [b[0]*b[1], b[0]*b[2], b[2]*b[1]]])
    bs = sorted(b)
    return area + bs[0] * bs[1]

with open("input") as f:
    boxes = [[int(d) for d in l.strip().split('x')] for l in f.readlines()]
    print sum([box_sq_feet(b) for b in boxes])
