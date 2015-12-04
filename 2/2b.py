#!/usr/bin/env python
import sys

def box_area(b):
    area = sum([2 * a for a in [b[0]*b[1], b[0]*b[2], b[2]*b[1]]])
    bs = sorted(b)
    return area + bs[0] * bs[1]

def box_volume(b):
    return b[0] * b[1] * b[2]

def box_shortest_around(b):
    bs = sorted(b)
    return bs[0] * 2 + bs[1] * 2

def bow_length(b):
    return box_volume(b) + box_shortest_around(b)

#test_box_1 = [2, 3, 4]
#print "test box 1 volume: %d" % box_volume(test_box_1)
#print "test box 1 shortest: %d" % box_shortest_around(test_box_1)
#print "test box 1 bows: %d" % bow_length(test_box_1)
#test_box_2 = [1, 1, 10]
#print "test box 2 volume: %d" % box_volume(test_box_2)
#print "test box 2 shortest: %d" % box_shortest_around(test_box_2)
#print "test box 2 bows: %d" % bow_length(test_box_2)
#test_box_3 = [30, 28, 5]
#print "test box 3 volume: %d" % box_volume(test_box_3)
#print "test box 3 shortest: %d" % box_shortest_around(test_box_3)
#print "test box 3 bows: %d" % bow_length(test_box_3)
#sys.exit(0)

with open("input") as f:
    boxes = [[int(d) for d in l.strip().split('x')] for l in f.readlines()]
    wrapping = sum([box_area(b) for b in boxes])
    bows = sum([bow_length(b) for b in boxes])
    print "wrapping: %d, bows: %d" % (wrapping, bows)
