#!/usr/bin/env python

# Was fun to do without regexes while exploring somewhat silly ways to check each requirement

def check_double(x, y):
    count, last = x
    if y == last:
        count += 1
    last = y
    return (count, last)

def all_pairs(s):
    for i in range(0,len(s)-1):
        yield s[i:i+2]

def nice(strings):
    nice_ones = list()
    for s in strings:
        # at least three of aeiou
        vowels = len([c for c in s if c in 'aeiou'])
        # at least one double
        doubles = reduce(check_double, s, (0, ''))[:1][0]
        # nothing blacklisted (ab, cd, pq, or xy)
        blacklisted = len([pair for pair in all_pairs(s) if pair in ['ab', 'cd', 'pq', 'xy']])
        if vowels > 2 and doubles > 0 and blacklisted == 0:
            nice_ones.append(s)
    return nice_ones

def nice2(strings):
    nice_ones = list()
    for s in strings:
        # two pairs separated by a character
        # at least one double with a character that separates
        double = False
        pair = False
        for i in range(0, len(s)):
            if s[i] == s[i+2:i+3]:  # silly way to avoid out of range
               double = True
            if s[i+2:len(s)].find(s[i:i+2]) >= 0:
               pair = True
        if double and pair:
            nice_ones.append(s)
    return nice_ones


#print 'nice ugknbfddgicrmopn: %d' % len(nice(['ugknbfddgicrmopn']))
#print 'nice aaa: %d' % len(nice(['aaa']))
#print 'nice jchzalrnumimnmhp: %d' % len(nice(['jchzalrnumimnmhp']))
#print 'nice haegwjzuvuyypxyu: %d' % len(nice(['haegwjzuvuyypxyu']))
##print 'nice dvszwmarrgswjxmb: %d' % len(nice(['dvszwmarrgswjxmb']))

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
