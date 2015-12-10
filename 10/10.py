#!/usr/bin/env python

from itertools import groupby

# Really should memorize what's available in itertools. 
# This version is actually much slower though!

def do(inp):
    return ''.join([str(len(list(it))) + what for what, it in groupby(inp)])

inp = '1113122113'
for i in range(40):
    inp = do(inp)
print len(inp)
inp = '1113122113'
for i in range(50):
    inp = do(inp)
print len(inp)
