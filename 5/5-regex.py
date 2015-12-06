#!/usr/bin/env python

import re

# After working on 5 for a few I realized that regexes would be so much easier.
# Had to finish without using them, had to do it again. :) 
# Should have done it in perl instead though, the thing I miss the most is the
# tight integration of regexes.

def nice(strings):
    nice_ones = list()
    for s in strings:
        if (
              re.match(r"(.*[aeiou]){3}", s) is not None 
              and re.match(r".*(.)\1", s) is not None
              and re.match(r".*(ab|cd|pq|xy)", s) is None
           ):
            nice_ones.append(s)
    return nice_ones

def nice2(strings):
    nice_ones = list()
    for s in strings:
        if (
              re.match(r".*(..).*\1", s) is not None
              and re.match(r".*(.).\1", s) is not None
           ):
            nice_ones.append(s)
    return nice_ones

#print 'nice ugknbfddgicrmopn: %d' % len(nice(['ugknbfddgicrmopn']))
#print 'nice aaa: %d' % len(nice(['aaa']))
#print 'nice jchzalrnumimnmhp: %d' % len(nice(['jchzalrnumimnmhp']))
#print 'nice haegwjzuvuyypxyu: %d' % len(nice(['haegwjzuvuyypxyu']))
#print 'nice dvszwmarrgswjxmb: %d' % len(nice(['dvszwmarrgswjxmb']))
#
#print 'nice2 aaa: %d' % len(nice2(['aaa']))
#print 'nice2 xyx: %d' % len(nice2(['aaa']))
#print 'nice2 qjhvhtzxzqqjkmpb: %d' % len(nice2(['qjhvhtzxzqqjkmpb']))
#print 'nice2 xxyxx: %d' % len(nice2(['xxyxx']))
#print 'nice2 uurcxstgmygtbstg: %d' % len(nice2(['uurcxstgmygtbstg']))
#print 'nice2 ieodomkazucvgmuy: %d' % len(nice2(['ieodomkazucvgmuy']))

with open('input') as f:
    strings = [s.strip() for s in f.readlines()]
    print len(nice(strings))
    print len(nice2(strings))
