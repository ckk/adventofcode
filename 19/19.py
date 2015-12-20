#!/usr/bin/env python

import sys
import re
from collections import defaultdict

# not sure this would find the shortest amount of steps in the general case
# it finds plenty of solutions with the same length, added an early termination
# was probably no nooed to use recursion even
def rev_fabricate(initial, replacements, count=0):
    #print "rev_fabricate: initial: %s count: %d" % (initial, count)
    counts = []
    for rfrom, rtos in replacements.items():
        for rto in rtos:
            #print "rev_fabricate initial %s, count: %d, %s => %s" % (initial, count, rfrom, rto)
            hit = initial.find(rfrom)
            while hit > -1:
                new_molecule = initial[0:hit] + rto + initial[hit+len(rfrom):]
                #print "rev_fabricate count %d hit %d new_molecule: %s" % (count, hit, new_molecule)
                if new_molecule == 'e':
                    print "rev_fabricate found it at %d from %s" % (count + 1, initial)
                    sys.exit(0) # the first one is good enough apparently, and it takes forever otherwise
                    return count+1
                counts.append(rev_fabricate(new_molecule, replacements, count+1))
                hit = initial.find(rfrom, hit+len(rfrom))
    if len(counts) > 0:
        return min(counts)
    else:
        return 1042
         

def do(input_file):
    with open(input_file) as f:
        strings = [s.strip() for s in f.readlines()]
    replacements = defaultdict(lambda: [])
    molecule = ''
    for s in strings:
        repl_match = re.match(r"^(\w+) => (\w+)$", s)
        if repl_match is not None:
            rfrom, rto = repl_match.groups()
            replacements[rfrom].append(rto)
        else:
            if s != '':
                molecule = s
    print "replacements", replacements
    print "molecule", molecule
    # calibrate (part 1)
    molecules = set()
    for rfrom, rtos in replacements.items():
        for rto in rtos:
            #print "%s => %s" % (rfrom, rto)
            hit = molecule.find(rfrom)
            while hit > -1:
                new_molecule = molecule[0:hit] + rto + molecule[hit+len(rfrom):]
                #print "hit, new_molecule:", hit, new_molecule
                molecules.add(new_molecule)
                hit = molecule.find(rfrom, hit+len(rfrom))
    #print "molecules", molecules
    print len(molecules)
    # fabricate (part 2)
    rev_replacements = defaultdict(lambda: [])
    for rfrom, rtos in replacements.items():
        for rto in rtos:
            rev_replacements[rto].append(rfrom)
    print rev_fabricate(molecule, rev_replacements)
    

# test
#do('input-test')

do('input')
