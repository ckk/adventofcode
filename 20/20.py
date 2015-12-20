#!/usr/bin/env python

# spent a lot of time trying to do this cleverly by soething that would converge on the correct
# solution. Didn't work out very well. Here's some brute force instead.

def do(target):
    upper = target / 10 # no need to go above this, needlessly high actually but fast enough anyway
    houses = [ 0 for x in range(upper+1) ]
    houses2 = [ 0 for x in range(upper+1) ]
    for n in range(1,upper):
        for house in range(n,upper,n):
            houses[house] += n*10
        for house in range(n, min(51*n,upper), n):
            houses2[house] += n*11
    house = 0
    while houses[house] < target:
        house += 1
    print "House for target %d: %d" % (target, house)
    house = 0
    while houses2[house] < target:
        house += 1
    print "House for target with lazy elves %d: %d" % (target, house)

do(150) # 8
do(1500) # 60
do(15000) # 480
do(150000) # 4320
do(33100000) # ?
